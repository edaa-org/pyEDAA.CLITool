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
"""This module contains the CLI abstraction layer for Active-HDL."""
from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument  import StringArgument, PathArgument
from pyTooling.CLIAbstraction.Flag      import LongFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import ShortTupleFlag
from pyEDAA.CLITool                     import ToolMixIn


@export
class VHDLLibraryTool(Executable, ToolMixIn):
	"""Abstraction of Active-HDL's VHDL library management tool ``vlib``."""

	_executableNames = {
		"Linux":   "vlib",
		"Windows": "vlib.exe"
	}

	@CLIArgument()
	class ValueLibraryName(StringArgument):
		"""Name of the VHDL library."""


@export
class VHDLCompiler(Executable, ToolMixIn):
	"""Abstraction of Active-HDL's VHDL compiler ``vcom``."""

	_executableNames = {
		"Linux":   "vcom",
		"Windows": "vcom.exe"
	}

	@CLIArgument()
	class FlagNoRangeCheck(LongFlag, name="norangecheck"): ...

	@CLIArgument()
	class SwitchVHDLVersion(StringArgument, pattern="-{0}"):
		"""Option to set the VHDL language revision."""

	@CLIArgument()
	class SwitchVHDLLibrary(ShortTupleFlag, name="work"):
		"""
		Option to set the VHDL library the design file is compiled into.

		Also known as *working library*.
		"""

	@CLIArgument()
	class ArgSourceFile(PathArgument):
		"""The path to a VHDL source file."""

	# -reorder                      enables automatic file ordering
	# -O[0 | 1 | 2 | 3]             set optimization level
	# -93                                conform to VHDL 1076-1993
	# -2002                              conform to VHDL 1076-2002 (default)
	# -2008                              conform to VHDL 1076-2008
	# -relax                             allow 32-bit integer literals
	# -incr                              switching compiler to fast incremental mode


@export
class VHDLSimulator(Executable, ToolMixIn):
	"""Abstraction of Active-HDL's simulator ``vsim``."""

	_executableNames = {
		"Linux":   "vsim",
		"Windows": "vsim.exe"
	}

	@CLIArgument()
	class SwitchBatchCommand(ShortTupleFlag, name="do"):
		"""Tcl command(s) to execute in the simulator."""
