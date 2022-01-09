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
"""This module contains the CLI abstraction layer for Vivado."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument  import ShortFlagArgument, ShortTupleArgument, ShortValuedFlagArgument, StringArgument
from pyEDAA.CLITool                     import ToolMixIn


@export
class XElab(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "xelab",
		"Windows": "xelab.bat"
	}

	@CLIOption
	class FlagRangeCheck(ShortFlagArgument, name="rangecheck"): ...

	@CLIOption
	class SwitchMultiThreading(ShortTupleArgument, name="mt"): ...

	@CLIOption
	class SwitchVerbose(ShortTupleArgument, name="verbose"): ...

	@CLIOption
	class SwitchDebug(ShortTupleArgument, name="debug"): ...

	# class SwitchVHDL2008(ShortFlagArgument):
	# 	_name =    "vhdl2008"
	# 	_value =  None

	@CLIOption
	class SwitchOptimization(ShortValuedFlagArgument, name="O"): ...
		# _pattern = "--{0}{1}"

	@CLIOption
	class SwitchTimeResolution(ShortTupleArgument, name="timeprecision_vhdl"): ...

	@CLIOption
	class SwitchProjectFile(ShortTupleArgument, name="prj"): ...

	@CLIOption
	class SwitchLogFile(ShortTupleArgument, name="log"): ...

	@CLIOption
	class SwitchSnapshot(ShortTupleArgument, name="s"): ...

	@CLIOption
	class ArgTopLevel(StringArgument): ...


@export
class XSim(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "xsim",
		"Windows": "xsim.bat"
	}

	@CLIOption
	class SwitchLogFile(ShortTupleArgument, name="log"): ...

	@CLIOption
	class FlagGuiMode(ShortFlagArgument, name="gui"): ...

	@CLIOption
	class SwitchTclBatchFile(ShortTupleArgument, name="tclbatch"): ...

	@CLIOption
	class SwitchWaveformFile(ShortTupleArgument, name="view"): ...

	@CLIOption
	class SwitchSnapshot(StringArgument): ...


@export
class Synth(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vivado",
		"Windows": "vivado.bat"
	}

	@CLIOption
	class SwitchLogFile(ShortTupleArgument, name="log"): ...

	@CLIOption
	class SwitchSourceFile(ShortTupleArgument, name="source"): ...

	@CLIOption
	class SwitchMode(ShortTupleArgument, name="mode"): ...
		# _value =  "batch"
