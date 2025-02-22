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
# Copyright 2017-2025 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""Unit tests for executable ``ghdl`` inside a container run via Docker."""
from pathlib import Path
from typing  import Optional as Nullable

from pytest                 import mark
from unittest               import TestCase

from pyEDAA.CLITool.GHDL    import GHDL
from pyEDAA.CLITool.Docker  import Docker
from .                      import Helper


class GHDLInDocker(Docker, GHDL):
	def __init__(self, executablePath: Nullable[Path] = None, binaryDirectoryPath: Nullable[Path] = None, dryRun: bool = False) -> None:
		super().__init__(executablePath, binaryDirectoryPath, dryRun)

		self.__cliParameters__[Docker.ValueCommand] = Docker.ValueCommand("ghdl")


class CommonOptions(TestCase, Helper):
	@mark.xfail
	def test_Help(self) -> None:
		tool = GHDLInDocker(dryRun=True)
		tool[GHDL.CommandHelp] = True
		tool[Docker.CommandContainer] = True
		tool[Docker.CommandRun] = True
		tool[Docker.FlagRemoveContainer] = True
		tool[Docker.ValueImageName] = "ghdl:latest"

		executable = self.getExecutablePath("docker")
		self.assertEqual(f"[\"{executable}\", \"container\", \"run\", \"--rm\", \"ghdl:latest\", \"ghdl\", \"help\"]", repr(tool))

	@mark.xfail
	def test_Version(self) -> None:
		tool = GHDLInDocker(dryRun=True)
		tool[Docker.CommandContainer] = True
		tool[Docker.CommandRun] = True
		tool[Docker.FlagRemoveContainer] = True
		tool[Docker.ValueImageName] = "ghdl:latest"
		tool[GHDL.CommandVersion] = True

		executable = self.getExecutablePath("docker")
		self.assertEqual(f"[\"{executable}\", \"container\", \"run\", \"--rm\", \"ghdl:latest\", \"ghdl\", \"version\"]", repr(tool))


class Analyze(TestCase, Helper):
	@mark.xfail
	def test_AnalyzeFile(self) -> None:
		tool = GHDLInDocker(dryRun=True)
		tool[tool.CommandAnalyze] = True
		tool[tool.FlagVHDLStandard] = "08"
		tool[tool.FlagSynopsys] = True
		tool[tool.FlagRelaxed] = True
		tool[tool.FlagExplicit] = True
		tool[tool.FlagMultiByteComments] = True
		tool[tool.FlagLibrary] = "lib_Test"

		executable = self.getExecutablePath("docker")
		self.assertEqual(f"[\"{executable}\", \"ghdl\", \"analyze\", \"--std=08\", \"-fsynopsys\", \"-frelaxed\", \"-fexplicit\", \"--work=lib_Test\", \"--mb-comments\"]", repr(tool))
