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
"""Unit tests for executable ``ghdl``."""
from os                   import getenv as os_getenv
from pathlib              import Path
from unittest             import TestCase

from pyEDAA.CLITool.GHDL  import GHDL, GHDLVersion
from .                    import Helper

class VersionString(TestCase):
	def test_ReleaseVersion(self) -> None:
		versionLine =  "GHDL 6.0.0-dev (4.1.0.r1065.gd3ea86f11.dirty) [Dunoon edition]"
		compilerLine = " Compiled with GNAT Version: 15.2.0"
		backendLine =  " static elaboration, mcode JIT code generator"

		version = GHDLVersion(versionLine, compilerLine, backendLine)

		self.assertEqual(6, version.Major)
		self.assertEqual(0, version.Minor)
		self.assertEqual(0, version.Micro)
		self.assertTrue(version.Dev)
		self.assertEqual(1065, version.CommitsSinceLastTag)
		self.assertEqual("d3ea86f11", version.GitHash)
		# FIXME: self.assertTrue(version.Dirty)
		self.assertEqual("Dunoon edition", version.Edition)
		# TODO: GNAT version
		self.assertEqual("mcode", version.Backend)


class GHDLTestcases(TestCase, Helper):
	_binaryDirectoryPath = (Path(os_getenv("GHDL_PREFIX", default="/usr/lib/ghdl")) / "../../bin").resolve()


class CommonOptions(GHDLTestcases):
	def test_Help(self) -> None:
		print()

		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandHelp] = True

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"help\"]", repr(tool))

		helpText = tool.Help()
		print(helpText)

	def test_Version(self) -> None:
		print()

		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandVersion] = True

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"version\"]", repr(tool))

		version = tool.Version()
		print(str(version))
		print(repr(version))


class Analyze(GHDLTestcases):
	def test_Analyze(self) -> None:
		print()

		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagVHDLStandard] = "08"
		tool[tool.FlagSynopsys] = True
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagExplicit] = True
		tool[tool.FlagMultiByteComments] = True
		tool[tool.FlagLibrary] = "lib_Test"

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--work=lib_Test\", \"--mb-comments\"]", repr(tool))

		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(1, tool.Wait())

	def _GetAnalyzer(self) -> GHDL:
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagVHDLStandard] = "08"
		tool[tool.FlagSynopsys] = True
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagExplicit] = True
		tool[tool.FlagMultiByteComments] = True

		return tool

	def test_AnalyzeFaultyFile(self) -> None:
		print()

		self.maxDiff = None

		path = Path("tests/project/designB/file_B1.vhdl")

		tool = self._GetAnalyzer()
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagLibrary] = "lib_Test"
		tool[tool.OptionPaths] = (path, )

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--work=lib_Test\", \"--mb-comments\", \"{path!s}\"]", repr(tool))

		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(1, tool.Wait())
		self.assertEqual(1, tool.ExitCode)

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
			tool = analyzer.GetGHDLAsAnalyzer()
			tool[tool.FlagLibrary] = "libCommon"
			tool[tool.OptionPaths] = (file, )
			tool.StartProcess()
			for line in tool.GetLineReader():
				print(line)

			self.assertEqual(0, tool.Wait())
			self.assertEqual(0, tool.ExitCode)

		for file in designFiles:
			print(f"analyze '{file}'")
			tool = analyzer.GetGHDLAsAnalyzer()
			tool[tool.FlagLibrary] = "libDesign"
			tool[tool.OptionPaths] = (file, )
			tool.StartProcess()
			for line in tool.GetLineReader():
				print(line)

			self.assertEqual(0, tool.Wait())

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
		tool = analyzer.GetGHDLAsAnalyzer()
		tool[tool.FlagLibrary] = "libCommon"
		tool[tool.OptionPaths] = libraryFiles
		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(0, tool.Wait())

		tool = analyzer.GetGHDLAsAnalyzer()
		tool[tool.FlagLibrary] = "libDesign"
		tool[tool.OptionPaths] = designFiles
		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)

		self.assertEqual(0, tool.Wait())
