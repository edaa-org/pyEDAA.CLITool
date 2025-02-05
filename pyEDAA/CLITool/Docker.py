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
# Copyright 2021-2025 Patrick Lehmann - Boetzingen, Germany                                                            #
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
from pyTooling.Decorators import export

from pyTooling.CLIAbstraction            import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument   import ExecutableArgument, StringArgument
from pyTooling.CLIAbstraction.Command    import CommandArgument
from pyTooling.CLIAbstraction.Flag       import LongFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import LongTupleFlag


@export
class Docker(Executable):
	_executableNames = {
		"Darwin":  "docker",
		"FreeBSD": "docker",
		"Linux":   "docker",
		"Windows": "docker.exe"
	}

	# 'version' sub commands and options
	@CLIArgument()
	class CommandVersion(CommandArgument, name="version"): ...

	# 'container' sub commands and options
	@CLIArgument()
	class CommandContainer(CommandArgument, name="container"): ...

	@CLIArgument()
	class CommandRun(CommandArgument, name="run"): ...

	@CLIArgument()
	class FlagContainerName(LongTupleFlag, name="name"): ...

	@CLIArgument()
	class FlagRemoveContainer(LongFlag, name="rm"): ...

	@CLIArgument()
	class FlagMount(LongTupleFlag, name="mount"): ...

	@CLIArgument()
	class FlagVolume(LongTupleFlag, name="volume"): ...

	@CLIArgument()
	class ValueImageName(StringArgument): ...

	@CLIArgument()
	class ValueCommand(StringArgument): ...

	@CLIArgument()
	class Executable(ExecutableArgument): ...  # XXX: no argument here
