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
"""Unit tests for container execution via ``docker``."""
from pytest                 import mark
from sys                    import platform as sys_platform
from unittest               import TestCase

from pyEDAA.CLITool.Docker  import Docker
from .                      import Helper


@mark.skipif(sys_platform == "win32", reason="Don't run these tests on Windows.")
class CommonOptions(TestCase, Helper):
	def test_Version(self):
		tool = Docker(dryRun=True)
		tool[tool.CommandVersion] = True

		executable = self.getExecutablePath("docker")
		self.assertEqual(f"[\"{executable}\", \"version\"]", repr(tool))


@mark.skipif(sys_platform == "win32", reason="Don't run these tests on Windows.")
class Analyze(TestCase, Helper):
	def test_Alpine(self):
		tool = Docker(dryRun=True)
		tool[tool.CommandContainer] = True
		tool[tool.CommandRun] = True
		tool[tool.FlagRemoveContainer] = True
		tool[tool.ValueImageName] = "alpine:latest"

		executable = self.getExecutablePath("docker")
		self.assertEqual(f"[\"{executable}\", \"container\", \"run\", \"--rm\", \"alpine:latest\"]", repr(tool))
