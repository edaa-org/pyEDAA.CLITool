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
# Copyright 2014-2016 Technische Universität Dresden - Germany, Chair of VLSI-Design, Diagnostics and Architecture     #
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
"""This module contains the CLI abstraction layer for Quartus."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument  import StringArgument
from pyTooling.CLIAbstraction.Flag      import ShortFlag
from pyTooling.CLIAbstraction.ValuedFlag import ShortValuedFlag, LongValuedFlag
from pyEDAA.CLITool                     import ToolMixIn


@export
class Map(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "quartus_map",
		"Windows": "quartus_map.exe"
	}

	@CLIArgument()
	class ArgProjectName(StringArgument): ...

	@CLIArgument()
	class SwitchArgumentFile(ShortValuedFlag, name="f"): ...

	@CLIArgument()
	class SwitchDeviceFamily(LongValuedFlag, name="family"): ...

	@CLIArgument()
	class SwitchDevicePart(LongValuedFlag, name="part"): ...


@export
class TclShell(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "quartus_sh",
		"Windows": "quartus_sh.exe"
	}

	@CLIArgument()
	class SwitchShell(ShortFlag, name="s"): ...
