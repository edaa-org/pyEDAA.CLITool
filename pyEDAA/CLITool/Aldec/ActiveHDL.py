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
"""This module contains the CLI abstraction layer for Active-HDL."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument  import LongFlagArgument, ShortTupleArgument, StringArgument, PathArgument
from pyEDAA.CLITool                     import ToolMixIn


@export
class VHDLLibraryTool(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vlib",
		"Windows": "vlib.exe"
	}

	@CLIOption
	class ValueLibraryName(StringArgument): ...


@export
class VHDLCompiler(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vcom",
		"Windows": "vcom.exe"
	}

	@CLIOption
	class FlagNoRangeCheck(LongFlagArgument, name="norangecheck"): ...

	@CLIOption
	class SwitchVHDLVersion(StringArgument, pattern="-{0}"): ...

	@CLIOption
	class SwitchVHDLLibrary(ShortTupleArgument, name="work"): ...

	@CLIOption
	class ArgSourceFile(PathArgument): ...

	# -reorder                      enables automatic file ordering
	# -O[0 | 1 | 2 | 3]             set optimization level
	# -93                                conform to VHDL 1076-1993
	# -2002                              conform to VHDL 1076-2002 (default)
	# -2008                              conform to VHDL 1076-2008
	# -relax                             allow 32-bit integer literals
	# -incr                              switching compiler to fast incremental mode


@export
class VHDLSimulator(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vsim",
		"Windows": "vsim.exe"
	}

	@CLIOption
	class SwitchBatchCommand(ShortTupleArgument, name="do"): ...
