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
# Copyright 2017-2024 Patrick Lehmann - Boetzingen, Germany                                                            #
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
from sys                  import platform as sys_platform
from os                   import getenv as os_getenv
from pathlib              import Path
from unittest             import TestCase

from pyEDAA.CLITool.GHDL  import GHDL
from .                    import Helper


class GHDLTestcases(TestCase, Helper):
	_libraryDirectoryPath = Path(os_getenv("GHDL_PREFIX", default="/usr/local/lib/ghdl"))
	_binaryDirectoryPath = Path(os_getenv("GHDL_PREFIX", default="/usr/local/lib/ghdl")) / "../../bin"

	@classmethod
	def setUpClass(cls) -> None:
		# print(f"\nPlatform: {sys_platform}")
		if sys_platform in ("linux", "darwin"):
			if not cls._libraryDirectoryPath.exists():
				print(f"Creating lib/ghdl directory '{cls._libraryDirectoryPath}': ", end="")
				cls._libraryDirectoryPath.mkdir(parents=True)
				print(f"DONE" if cls._libraryDirectoryPath.exists() and cls._libraryDirectoryPath.is_dir() else f"FAILED")

			binaryDirectoryPath = cls._binaryDirectoryPath.resolve()
			if not binaryDirectoryPath.exists():
				print(f"Creating bin directory '{binaryDirectoryPath}': ", end="")
				binaryDirectoryPath.mkdir(parents=True)
				print(f"DONE" if binaryDirectoryPath.exists() and binaryDirectoryPath.is_dir() else f"FAILED")

			ghdlBinaryPath: Path = binaryDirectoryPath / "ghdl"
			print(f"Creating dummy file '{ghdlBinaryPath}': ", end="")
			ghdlBinaryPath.touch()
			print(f"DONE" if ghdlBinaryPath.exists() and ghdlBinaryPath.is_file() else f"FAILED")


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
		tool.Terminate()
		print(tool.ExitCode)

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

		tool = self._GetAnalyzer()
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagLibrary] = "lib_Test"
		tool[tool.OptionPaths] = (Path("project/designB/file_B1.vhdl"), )

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--work=lib_Test\", \"--mb-comments\", \"project\\designB\\file_B1.vhdl\"]", repr(tool))

		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)
		tool.Terminate()

		self.assertEqual(1, tool.ExitCode)

	def test_AnalyzeSingleFiles(self) -> None:
		print()

		libraryFiles = (
			Path("project/lib/file_P1.vhdl"),
			Path("project/lib/file_P2.vhdl"),
		)
		designFiles = (
			Path("project/designA/file_A1.vhdl"),
			Path("project/designA/file_A2.vhdl"),
		)

		analyzer = self._GetAnalyzer()
		for file in libraryFiles:
			tool = analyzer.GetGHDLAsAnalyzer()
			tool[tool.FlagLibrary] = "libCommon"
			tool[tool.OptionPaths] = (file, )
			tool.StartProcess()
			for line in tool.GetLineReader():
				print(line)
			tool.Terminate()

			self.assertEqual(0, tool.ExitCode)

		for file in designFiles:
			tool = analyzer.GetGHDLAsAnalyzer()
			tool[tool.FlagLibrary] = "libDesign"
			tool[tool.OptionPaths] = (file, )
			tool.StartProcess()
			for line in tool.GetLineReader():
				print(line)
			tool.Terminate()

			self.assertEqual(0, tool.ExitCode)

	def test_AnalyzeMultipleFiles(self) -> None:
		print()

		libraryFiles = (
			Path("project/lib/file_P1.vhdl"),
			Path("project/lib/file_P2.vhdl"),
		)
		designFiles = (
			Path("project/designA/file_A1.vhdl"),
			Path("project/designA/file_A2.vhdl"),
		)

		analyzer = self._GetAnalyzer()
		tool = analyzer.GetGHDLAsAnalyzer()
		tool[tool.FlagLibrary] = "libCommon"
		tool[tool.OptionPaths] = libraryFiles
		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)
		tool.Terminate()

		self.assertEqual(0, tool.ExitCode)

		tool = analyzer.GetGHDLAsAnalyzer()
		tool[tool.FlagLibrary] = "libDesign"
		tool[tool.OptionPaths] = designFiles
		tool.StartProcess()
		for line in tool.GetLineReader():
			print(line)
		tool.Terminate()

		self.assertEqual(0, tool.ExitCode)
