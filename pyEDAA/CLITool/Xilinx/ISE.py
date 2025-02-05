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
"""This module contains the CLI abstraction layer for ISE."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument  import StringArgument
from pyTooling.CLIAbstraction.Flag      import ShortFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import ShortTupleFlag
from pyEDAA.CLITool                     import ToolMixIn


@export
class Fuse(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "fuse",
		"Windows": "fuse.exe"
	}

	@CLIArgument()
	class FlagIncremental(ShortFlag, name="incremental"): ...

	# FlagIncremental = ShortFlagArgument(_name="incremntal")

	@CLIArgument()
	class FlagRangeCheck(ShortFlag, name="rangecheck"): ...

	@CLIArgument()
	class SwitchMultiThreading(ShortTupleFlag, name="mt"): ...

	@CLIArgument()
	class SwitchTimeResolution(ShortTupleFlag, name="timeprecision_vhdl"): ...

	@CLIArgument()
	class SwitchProjectFile(ShortTupleFlag, name="prj"): ...

	@CLIArgument()
	class SwitchOutputFile(ShortTupleFlag, name="o"): ...

	@CLIArgument()
	class ArgTopLevel(StringArgument): ...


@export
class ISESimulator(Executable):
	_executableNames = {
		"Linux":   "isim",
		"Windows": "isim.exe"
	}

	@CLIArgument()
	class SwitchLogFile(ShortTupleFlag, name="log"): ...

	@CLIArgument()
	class FlagGuiMode(ShortFlag, name="gui"): ...

	@CLIArgument()
	class SwitchTclBatchFile(ShortTupleFlag, name="tclbatch"): ...

	@CLIArgument()
	class SwitchWaveformFile(ShortTupleFlag, name="view"): ...


@export
class Xst(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "xst",
		"Windows": "xst.exe"
	}

	@CLIArgument()
	class SwitchIntStyle(ShortTupleFlag, name="intstyle"): ...

	@CLIArgument()
	class SwitchXstFile(ShortTupleFlag, name="ifn"): ...

	@CLIArgument()
	class SwitchReportFile(ShortTupleFlag, name="ofn"): ...


@export
class CoreGenerator(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "coregen",
		"Windows": "coregen.exe"
	}

	@CLIArgument()
	class FlagRegenerate(ShortFlag, name="r"): ...

	@CLIArgument()
	class SwitchProjectFile(ShortTupleFlag, name="p"): ...

	@CLIArgument()
	class SwitchBatchFile(ShortTupleFlag, name="b"): ...
