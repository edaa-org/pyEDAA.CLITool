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
# Copyright 2021-2021 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""This module contains the CLI abstraction layer for `GHDL <https://github.com/ghdl/ghdl>`__."""
from pyTooling.CLIAbstraction            import CLIOption
from pyTooling.CLIAbstraction            import Executable
from pyTooling.CLIAbstraction.Argument   import (
	ExecutableArgument, CommandArgument,
	ShortFlagArgument, LongFlagArgument,
	ShortValuedFlagArgument, LongValuedFlagArgument,
	LongTupleArgument,
	StringArgument
)


class Docker(Executable):
	_executableNames = {
		"Linux":   "docker",
		"Windows": "docker.exe"
	}

	# 'version' sub commands and options
	@CLIOption()
	class CommandVersion(CommandArgument, name="version"): ...

	# 'container' sub commands and options
	@CLIOption()
	class CommandContainer(CommandArgument, name="container"): ...

	@CLIOption()
	class CommandRun(CommandArgument, name="run"): ...

	@CLIOption()
	class FlagContainerName(LongTupleArgument, name="name"): ...

	@CLIOption()
	class FlagRemoveContainer(LongFlagArgument, name="rm"): ...

	@CLIOption()
	class FlagMount(LongTupleArgument, name="mount"): ...

	@CLIOption()
	class FlagVolume(LongTupleArgument, name="volume"): ...

	@CLIOption()
	class ValueImageName(StringArgument): ...

	@CLIOption()
	class ValueCommand(StringArgument): ...

	@CLIOption()
	class Executable(ExecutableArgument): ...  # XXX: no argument here
