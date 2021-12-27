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
# Copyright 2017-2021 Patrick Lehmann - Boetzingen, Germany                                                            #
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
from os                   import environ as os_environ
from pathlib              import Path
from unittest             import TestCase

from pyEDAA.CLITool.GHDL  import GHDL


class CommonOptions(TestCase):
	_binaryDirectoryPath = Path(os_environ["GHDL_PREFIX"]) / "bin"

	def test_Help(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagHelp] = True

		self.assertEqual(f"[\"{self._binaryDirectoryPath}\ghdl.exe\", \"--help\"]", repr(tool))

	def test_Version(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagVersion] = True

		self.assertEqual(f"[\"{self._binaryDirectoryPath}\ghdl.exe\", \"--version\"]", repr(tool))


class Analyze(TestCase):
	_binaryDirectoryPath = Path(os_environ["GHDL_PREFIX"]) / "bin"

	def test_AnalyzeFile(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagVHDlStandard] = "08"
		tool[tool.FlagSynopsys] = True
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagExplicit] = True
		tool[tool.FlagMultiByteComments] = True
		tool[tool.FlagLibrary] = "lib_Test"

		self.assertEqual(f"[\"{self._binaryDirectoryPath}\ghdl.exe\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--mb-comments\", \"--work=lib_Test\"]", repr(tool))

	def test_DeriveAnalyzer(self):
		tool = GHDL(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagVHDlStandard] = "08"
		tool[tool.FlagSynopsys] = True
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagExplicit] = True
		tool[tool.FlagMultiByteComments] = True

		derived = tool.DeriveForAnalyze()
		derived[derived.FlagLibrary] = "lib_Test"

		self.assertEqual(f"[\"{self._binaryDirectoryPath}\ghdl.exe\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--mb-comments\", \"--work=lib_Test\"]", repr(derived))

