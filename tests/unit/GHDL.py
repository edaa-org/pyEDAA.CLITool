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
# Copyright 2017-2023 Patrick Lehmann - Boetzingen, Germany                                                            #
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


class CommonOptions(TestCase, Helper):
	_binaryDirectoryPath = Path(os_getenv("GHDL_PREFIX", default="/usr/local")) / "bin"

	@classmethod
	def setUpClass(cls) -> None:
		print(f"\nPlatform: {sys_platform}")
		if sys_platform in ("linux", "darwin"):
			ghdlBinaryPath: Path = cls._binaryDirectoryPath / "ghdl"
			print(f"Creating dummy file '{ghdlBinaryPath}': ", end="")
			ghdlBinaryPath.touch()
			print(f"DONE" if ghdlBinaryPath.exists() else f"FAILED")

	def test_Help(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandHelp] = True

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"help\"]", repr(tool))

	def test_Version(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandVersion] = True

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"version\"]", repr(tool))


class Analyze(TestCase, Helper):
	_binaryDirectoryPath = Path(os_getenv("GHDL_PREFIX", default="/usr/local")) / "bin"

	@classmethod
	def setUpClass(cls) -> None:
		print(f"\nPlatform: {sys_platform}")
		if sys_platform in ("linux", "darwin"):
			ghdlBinaryPath: Path = cls._binaryDirectoryPath / "ghdl"
			print(f"Creating dummy file '{ghdlBinaryPath}': ", end="")
			ghdlBinaryPath.touch()
			print(f"DONE" if ghdlBinaryPath.exists() else f"FAILED")

	def test_AnalyzeFile(self):
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

	def test_DeriveAnalyzer(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagVHDLStandard] = "08"
		tool[tool.FlagSynopsys] = True
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagExplicit] = True
		tool[tool.FlagMultiByteComments] = True

		derived = tool.GetGHDLAsAnalyzer()
		derived[derived.FlagLibrary] = "lib_Test"

		executable = self.getExecutablePath("ghdl", self._binaryDirectoryPath)
		self.assertEqual(f"[\"{executable}\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--work=lib_Test\", \"--mb-comments\"]", repr(derived))
