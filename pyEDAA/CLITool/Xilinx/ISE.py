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
"""This module contains the CLI abstraction layer for ISE."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument  import ShortFlagArgument, ShortTupleArgument, StringArgument
from pyEDAA.CLITool                     import ToolMixIn


@export
class Fuse(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "fuse",
		"Windows": "fuse.exe"
	}

	@CLIOption
	class FlagIncremental(ShortFlagArgument, name="incremental"): ...

	# FlagIncremental = ShortFlagArgument(_name="incremntal")

	@CLIOption
	class FlagRangeCheck(ShortFlagArgument, name="rangecheck"): ...

	@CLIOption
	class SwitchMultiThreading(ShortTupleArgument, name="mt"): ...

	@CLIOption
	class SwitchTimeResolution(ShortTupleArgument, name="timeprecision_vhdl"): ...

	@CLIOption
	class SwitchProjectFile(ShortTupleArgument, name="prj"): ...

	@CLIOption
	class SwitchOutputFile(ShortTupleArgument, name="o"): ...

	@CLIOption
	class ArgTopLevel(StringArgument): ...


@export
class ISESimulator(Executable):
	_executableNames = {
		"Linux":   "isim",
		"Windows": "isim.exe"
	}

	@CLIOption
	class SwitchLogFile(ShortTupleArgument, name="log"): ...

	@CLIOption
	class FlagGuiMode(ShortFlagArgument, name="gui"): ...

	@CLIOption
	class SwitchTclBatchFile(ShortTupleArgument, name="tclbatch"): ...

	@CLIOption
	class SwitchWaveformFile(ShortTupleArgument, name="view"): ...


@export
class Xst(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "xst",
		"Windows": "xst.exe"
	}

	@CLIOption
	class SwitchIntStyle(ShortTupleArgument, name="intstyle"): ...

	@CLIOption
	class SwitchXstFile(ShortTupleArgument, name="ifn"): ...

	@CLIOption
	class SwitchReportFile(ShortTupleArgument, name="ofn"): ...


@export
class CoreGenerator(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "coregen",
		"Windows": "coregen.exe"
	}

	@CLIOption
	class FlagRegenerate(ShortFlagArgument, name="r"): ...

	@CLIOption
	class SwitchProjectFile(ShortTupleArgument, name="p"): ...

	@CLIOption
	class SwitchBatchFile(ShortTupleArgument, name="b"): ...
