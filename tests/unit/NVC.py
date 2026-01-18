# ==================================================================================================================== #
#              _____ ____    _        _      ____ _     ___ _____           _                                          #
#  _ __  _   _| ____|  _ \  / \      / \    / ___| |   |_ _|_   _|__   ___ | |                                         #
# | '_ \| | | |  _| | | | |/ _ \    / _ \  | |   | |    | |  | |/ _ \ / _ \| |                                         #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ | |___| |___ | |  | | (_) | (_) | |                                         #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)____|_____|___| |_|\___/ \___/|_|                                         #
# |_|    |___/                                                                                                         #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2026 Patrick Lehmann - Boetzingen, Germany                                                            #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""Unit tests for executable ``nvc``."""
from os                   import getenv as os_getenv
from pathlib              import Path
from unittest             import TestCase

from pytest               import mark
from pyTooling.Platform   import CurrentPlatform

from pyEDAA.CLITool.NVC   import NVC, NVCVersion
from .                    import Helper


class VersionString(TestCase):
	def test_ReleaseVersion(self) -> None:
		versionLine = "nvc 1.18.2 (1.18.2.r0.g8893318a) (Using LLVM 21.1.5)"
		version = NVCVersion(versionLine)

		self.assertEqual(1, version.Major)
		self.assertEqual(18, version.Minor)
		self.assertEqual(2, version.Micro)
		self.assertEqual(0, version.CommitsSinceLastTag)
		self.assertEqual("8893318a", version.GitHash)
		self.assertEqual("LLVM", version.Backend)


class NVCTestcases(TestCase, Helper):
	if CurrentPlatform.IsNativeWindows:
		_binaryDirectoryPath = Path(os_getenv("NVC_BINDIR", default="C:\\Program Files\\NVC\\bin")).resolve()
	else:
		_binaryDirectoryPath = Path(os_getenv("NVC_BINDIR", default="/usr/bin")).resolve()


class CommonOptions(NVCTestcases):
	@mark.skipif(CurrentPlatform.IsCI and not CurrentPlatform.IsNativeLinux, reason="Runs only on Linux.")
	def test_Help(self) -> None:
		print()

		tool = NVC(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandHelp] = True

		executable = self.getExecutablePath("nvc", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"--help\"]", repr(tool))

		helpText = tool.Help()
		print(helpText)

	@mark.skipif(CurrentPlatform.IsCI and not CurrentPlatform.IsNativeLinux, reason="Runs only on Linux.")
	def test_Version(self) -> None:
		print()

		tool = NVC(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandVersion] = True

		executable = self.getExecutablePath("nvc", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"--version\"]", repr(tool))

		version = tool.Version()
		print(str(version))
		print(repr(version))

	# TODO: --do <TCL file>

class Analyze(NVCTestcases):
	@mark.skipif(CurrentPlatform.IsCI and not CurrentPlatform.IsNativeLinux, reason="Runs only on Linux.")
	def test_Analyze(self) -> None:
		print()

		tool = NVC(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagVHDLStandard] = "08"
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagLibrary] = "lib_Test"

		executable = self.getExecutablePath("nvc", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"--std=08\", \"--work=lib_Test\", \"-a\", \"--relaxed\"]", repr(tool))

		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(1, tool.Wait())

	def _GetAnalyzer(self) -> NVC:
		tool = NVC(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagVHDLStandard] = "08"
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagRelaxed] = True

		return tool

	@mark.skipif(CurrentPlatform.IsCI and not CurrentPlatform.IsNativeLinux, reason="Runs only on Linux.")
	def test_AnalyzeFaultyFile(self) -> None:
		print()

		self.maxDiff = None

		path = Path("tests/project/designB/file_B1.vhdl")

		tool = self._GetAnalyzer()
		tool[tool.FlagLibrary] = "lib_Test"
		tool[tool.OptionPaths] = (path, )

		executable = self.getExecutablePath("nvc", self._binaryDirectoryPath)
		print(Path.cwd())
		print(repr(tool))
		self.assertEqual(f"[\"{executable}\", \"--std=08\", \"--work=lib_Test\", \"-a\", \"{path!s}\", \"--relaxed\"]", repr(tool))

		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(1, tool.Wait())
		self.assertEqual(1, tool.ExitCode)

	@mark.skipif(CurrentPlatform.IsCI and not CurrentPlatform.IsNativeLinux, reason="Runs only on Linux.")
	def test_AnalyzeSingleFiles(self) -> None:
		print()

		libraryFiles = (
			Path("tests/project/lib/file_P1.vhdl"),
			Path("tests/project/lib/file_P2.vhdl"),
		)
		designFiles = (
			Path("tests/project/designA/file_A1.vhdl"),
			Path("tests/project/designA/file_A2.vhdl"),
		)

		analyzer = self._GetAnalyzer()
		for file in libraryFiles:
			print(f"analyze '{file}'")
			tool = analyzer.GetNVCAsAnalyzer()
			tool[tool.FlagLibrary] = "libCommon"
			tool[tool.OptionPaths] = (file, )
			tool.StartProcess()
			for line in tool.GetLineReader():
				print(line)

			self.assertEqual(0, tool.Wait())
			self.assertEqual(0, tool.ExitCode)

		for file in designFiles:
			print(f"analyze '{file}'")
			tool = analyzer.GetNVCAsAnalyzer()
			tool[tool.FlagLibrarySearchPath] = "."
			tool[tool.FlagLibrary] = "libDesign"
			tool[tool.OptionPaths] = (file, )
			tool.StartProcess()
			for line in tool.GetLineReader():
				print(line)

			self.assertEqual(0, tool.Wait())

	@mark.skipif(CurrentPlatform.IsCI and not CurrentPlatform.IsNativeLinux, reason="Runs only on Linux.")
	def test_AnalyzeMultipleFiles(self) -> None:
		print()

		libraryFiles = (
			Path("tests/project/lib/file_P1.vhdl"),
			Path("tests/project/lib/file_P2.vhdl"),
		)
		designFiles = (
			Path("tests/project/designA/file_A1.vhdl"),
			Path("tests/project/designA/file_A2.vhdl"),
		)

		analyzer = self._GetAnalyzer()
		tool = analyzer.GetNVCAsAnalyzer()
		tool[tool.FlagLibrary] = "libCommon"
		tool[tool.OptionPaths] = libraryFiles
		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(0, tool.Wait())

		tool = analyzer.GetNVCAsAnalyzer()
		tool[tool.FlagLibrarySearchPath] = "."
		tool[tool.FlagLibrary] = "libDesign"
		tool[tool.OptionPaths] = designFiles
		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(0, tool.Wait())
