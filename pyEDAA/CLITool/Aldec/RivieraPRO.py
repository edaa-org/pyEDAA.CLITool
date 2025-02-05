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
"""This module contains the CLI abstraction layer for Riviera-PRO."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument  import StringArgument, PathArgument
from pyTooling.CLIAbstraction.Flag      import ShortFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import ShortTupleFlag
from pyEDAA.CLITool                     import ToolMixIn


@export
class VHDLLibraryTool(Executable, ToolMixIn):
	"""Abstraction of Riviera-PRO's VHDL library management tool ``vlib``."""

	_executableNames = {
		"Linux":   "vlib",
		"Windows": "vlib.exe"
	}

	@CLIArgument()
	class SwitchLibraryName(StringArgument): ...


class VHDLCompiler(Executable, ToolMixIn):
	"""Abstraction of Riviera-PRO's VHDL compiler ``vcom``."""

	_executableNames = {
		"Linux":   "vcom",
		"Windows": "vcom.exe"
	}

	# class FlagNoRangeCheck(metaclass=LongFlagArgument):
	# 	_name =   "norangecheck"

	@CLIArgument()
	class SwitchVHDLVersion(StringArgument, pattern="-{0}"): ...

	@CLIArgument()
	class SwitchVHDLLibrary(ShortTupleFlag, name="work"): ...

	@CLIArgument()
	class ArgSourceFile(PathArgument): ...


@export
class VHDLSimulator(Executable, ToolMixIn):
	"""Abstraction of Riviera-PRO's HDL simulator ``vsim``."""

	_executableNames = {
		"Linux":   "vsim",
		"Windows": "vsim.exe"
	}

	@CLIArgument()
	class SwitchBatchCommand(ShortTupleFlag, name="do"):
		"""Specify a Tcl batch script for the batch mode."""

	@CLIArgument()
	class FlagCommandLineMode(ShortFlag, name="c"):
		"""Run simulation in command line mode."""

	@CLIArgument()
	class SwitchTimeResolution(ShortTupleFlag, name="t"):   # -t [1|10|100]fs|ps|ns|us|ms|sec  Time resolution limit
		"""Set simulation time resolution."""

	@CLIArgument()
	class SwitchTopLevel(StringArgument):
		"""The top-level for simulation."""
