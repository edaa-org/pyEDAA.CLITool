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
# Copyright 2017-2022 Patrick Lehmann - Boetzingen, Germany                                                            #
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
from pyTooling.CLIAbstraction           import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument  import StringArgument, StringListArgument
from pyTooling.CLIAbstraction.Flag      import ShortFlag
from pyTooling.CLIAbstraction.ValuedFlag import ShortValuedFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import ShortTupleFlag
from pyEDAA.CLITool                     import ToolMixIn


@export
class Vvgl(Executable):
	_executableNames = {
		"Windows": "unwrapped/win64.o/vvgl.exe"
	}

	@CLIArgument()
	class ValueWrappedExecutable(StringArgument):
		"""Executable to be wrapped by vvgl."""

	@CLIArgument()
	class Arguments(StringListArgument):
		"""List of arguments to be passed to the wrapped executable."""


@export
class XElab(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "xelab",
		"Windows": "xelab.bat"
	}

	@CLIArgument()
	class FlagRangeCheck(ShortFlag, name="rangecheck"): ...

	@CLIArgument()
	class SwitchMultiThreading(ShortTupleFlag, name="mt"): ...

	@CLIArgument()
	class SwitchVerbose(ShortTupleFlag, name="verbose"): ...

	@CLIArgument()
	class SwitchDebug(ShortTupleFlag, name="debug"): ...

	# class SwitchVHDL2008(ShortFlagArgument):
	# 	_name =    "vhdl2008"
	# 	_value =  None

	@CLIArgument()
	class SwitchOptimization(ShortValuedFlag, name="O"): ...
		# _pattern = "--{0}{1}"

	@CLIArgument()
	class SwitchTimeResolution(ShortTupleFlag, name="timeprecision_vhdl"): ...

	@CLIArgument()
	class SwitchProjectFile(ShortTupleFlag, name="prj"): ...

	@CLIArgument()
	class SwitchLogFile(ShortTupleFlag, name="log"): ...

	@CLIArgument()
	class SwitchSnapshot(ShortTupleFlag, name="s"): ...

	@CLIArgument()
	class ArgTopLevel(StringArgument): ...


@export
class XSim(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "xsim",
		"Windows": "xsim.bat"
	}

	@CLIArgument()
	class SwitchLogFile(ShortTupleFlag, name="log"): ...

	@CLIArgument()
	class FlagGuiMode(ShortFlag, name="gui"): ...

	@CLIArgument()
	class SwitchTclBatchFile(ShortTupleFlag, name="tclbatch"): ...

	@CLIArgument()
	class SwitchWaveformFile(ShortTupleFlag, name="view"): ...

	@CLIArgument()
	class SwitchSnapshot(StringArgument): ...


@export
class Synth(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vivado",
		"Windows": "vivado.bat"
	}

	@CLIArgument()
	class SwitchLogFile(ShortTupleFlag, name="log"): ...

	@CLIArgument()
	class SwitchSourceFile(ShortTupleFlag, name="source"): ...

	@CLIArgument()
	class SwitchMode(ShortTupleFlag, name="mode"): ...
		# _value =  "batch"
