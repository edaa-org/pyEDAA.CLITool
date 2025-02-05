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
"""This module contains the CLI abstraction layer for ModelSim."""
from enum import Enum

from flags import Flags

from pyTooling.Decorators               import export
from pyTooling.CLIAbstraction           import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument  import StringArgument
from pyTooling.CLIAbstraction.Flag      import ShortFlag
from pyTooling.CLIAbstraction.OptionalValuedFlag import OptionalValuedFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import ShortTupleFlag
from pyEDAA.CLITool                     import ToolMixIn


@export
class OptionalModelSimMinusArgument(OptionalValuedFlag, pattern="-{0}", patternWithValue="-{0} {1}"):
	pass


@export
class OptionalModelSimPlusArgument(OptionalValuedFlag, pattern="-{0}", patternWithValue="+{0} {1}"):
	pass


@export
class VHDLLibraryTool(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vlib",
		"Windows": "vlib.exe"
	}

	@CLIArgument()
	class ValueLibraryName(StringArgument):
		"""VHDL library name to create."""

@export
class VHDLCompilerCoverageOptions(Flags):
	__no_flags_name__ =   "Default"
	__all_flags_name__ =  "All"
	Statement =           "s"
	Branch =              "b"
	Condition =           "c"
	Expression =          "e"
	StateMachine =        "f"
	Toggle =              "t"

	def __str__(self) -> str:
		return "".join([i.value for i in self])


@export
class VHDLCompilerFSMVerbosityLevel(Enum):
	Default =         ""
	Basic =           "b"
	TransitionTable = "t"
	AnyWarning =      "w"

	def __str__(self) -> str:
		return self.value


@export
class VHDLCompiler(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vcom",
		"Windows": "vcom.exe"
	}

	@CLIArgument()
	class FlagTime(ShortFlag, name="time"):
		"""Print the compilation wall clock time."""

	@CLIArgument()
	class FlagExplicit(ShortFlag, name="explicit"): ...

	@CLIArgument()
	class FlagQuietMode(ShortFlag, name="quiet"):
		"""Do not report 'Loading...' messages."""

	@CLIArgument()
	class SwitchModelSimIniFile(ShortTupleFlag, name="modelsimini"): ...

	@CLIArgument()
	class FlagRangeCheck(ShortFlag, name="rangecheck"): ...

	@CLIArgument()
	class SwitchCoverage(OptionalModelSimPlusArgument, name="cover"): ...

	@CLIArgument()
	class FlagEnableFocusedExpressionCoverage(ShortFlag, name="coverfec"): ...

	@CLIArgument()
	class FlagDisableFocusedExpressionCoverage(ShortFlag, name="nocoverfec"): ...

	@CLIArgument()
	class FlagEnableRapidExpressionCoverage(ShortFlag, name="coverrec"): ...

	@CLIArgument()
	class FlagDisableRapidExpressionCoverage(ShortFlag, name="nocoverrec"): ...

	@CLIArgument()
	class FlagEnableRecognitionOfImplicitFSMResetTransitions(ShortFlag, name="fsmresettrans"): ...

	@CLIArgument()
	class FlagDisableRecognitionOfImplicitFSMResetTransitions(ShortFlag, name="nofsmresettrans"): ...

	@CLIArgument()
	class FlagEnableRecognitionOfSingleBitFSMState(ShortFlag, name="fsmsingle"): ...

	@CLIArgument()
	class FlagDisableRecognitionOfSingleBitFSMState(ShortFlag, name="nofsmsingle"): ...

	@CLIArgument()
	class FlagEnableRecognitionOfImplicitFSMTransitions(ShortFlag, name="fsmimplicittrans"): ...

	@CLIArgument()
	class FlagDisableRecognitionOfImplicitFSMTransitions(ShortFlag, name="nofsmimplicittrans"): ...

	@CLIArgument()
	class SwitchFSMVerbosityLevel(OptionalModelSimMinusArgument, name="fsmverbose"): ...

	@CLIArgument()
	class FlagReportAsNote(ShortTupleFlag, name="note"): ...

	@CLIArgument()
	class FlagReportAsError(ShortTupleFlag, name="error"): ...

	@CLIArgument()
	class FlagReportAsWarning(ShortTupleFlag, name="warning"): ...

	@CLIArgument()
	class FlagReportAsFatal(ShortTupleFlag, name="fatal"): ...

	@CLIArgument()
	class FlagRelaxLanguageChecks(ShortFlag, name="permissive"): ...

	@CLIArgument()
	class FlagForceLanguageChecks(ShortFlag, name="pedanticerrors"): ...

	@CLIArgument()
	class SwitchVHDLVersion(StringArgument, pattern="-{0}"): ...

	@CLIArgument()
	class ArgLogFile(ShortTupleFlag, name="l"): ...			# what's the difference to -logfile ?

	@CLIArgument()
	class SwitchVHDLLibrary(ShortTupleFlag, name="work"): ...

	# @CLIArgument()
	# class ArgSourceFile(PathArgument): ...


@export
class VHDLSimulator(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vsim",
		"Windows": "vsim.exe"
	}

	@CLIArgument()
	class FlagQuietMode(ShortFlag, name="quiet"):
		"""Run simulation in quiet mode. (Don't show 'Loading...' messages."""

	@CLIArgument()
	class FlagBatchMode(ShortFlag, name="batch"):
		"""Run simulation in batch mode."""

	@CLIArgument()
	class FlagGuiMode(ShortFlag, name="gui"):
		"""Run simulation in GUI mode."""

	@CLIArgument()
	class SwitchBatchCommand(ShortTupleFlag, name="do"):
		"""Specify a Tcl batch script for the batch mode."""

	@CLIArgument()
	class FlagCommandLineMode(ShortFlag, name="c"):
		"""Run simulation in command line mode."""

	@CLIArgument()
	class SwitchModelSimIniFile(ShortTupleFlag, name="modelsimini"):
		"""Specify the used 'modelsim.ini' file."""

	@CLIArgument()
	class FlagEnableOptimization(ShortFlag, name="vopt"):
		"""Enabled optimization while elaborating the design."""

	@CLIArgument()
	class FlagDisableOptimization(ShortFlag, name="novopt"):
		"""Disabled optimization while elaborating the design."""

	@CLIArgument()
	class FlagEnableOptimizationVerbosity(ShortFlag, name="vopt_verbose"):
		"""Enabled optimization while elaborating the design."""

	@CLIArgument()
	class FlagEnableKeepAssertionCountsForCoverage(ShortFlag, name="assertcover"): ...

	@CLIArgument()
	class FlagDisableKeepAssertionCountsForCoverage(ShortFlag, name="noassertcover"): ...

	@CLIArgument()
	class FlagEnableCoverage(ShortFlag, name="coverage"): ...

	@CLIArgument()
	class FlagDisableCoverage(ShortFlag, name="nocoverage"): ...

	@CLIArgument()
	class FlagEnablePSL(ShortFlag, name="psl"): ...

	@CLIArgument()
	class FlagDisablePSL(ShortFlag, name="nopsl"): ...

	@CLIArgument()
	class FlagEnableFSMDebugging(ShortFlag, name="fsmdebug"): ...

	@CLIArgument()
	class FlagReportAsNote(ShortTupleFlag, name="note"): ...

	@CLIArgument()
	class FlagReportAsError(ShortTupleFlag, name="error"): ...

	@CLIArgument()
	class FlagReportAsWarning(ShortTupleFlag, name="warning"): ...

	@CLIArgument()
	class FlagReportAsFatal(ShortTupleFlag, name="fatal"): ...

	@CLIArgument()
	class FlagRelaxLanguageChecks(ShortFlag, name="permissive"): ...

	@CLIArgument()
	class FlagForceLanguageChecks(ShortFlag, name="pedanticerrors"): ...

	@CLIArgument()
	class SwitchTimeResolution(ShortTupleFlag, name="t"):
		"""Set simulation time resolution."""
		# -t [1|10|100]fs|ps|ns|us|ms|sec  Time resolution limit

	@CLIArgument()
	class ArgLogFile(ShortTupleFlag, name="l"): ...
		# what's the difference to -logfile ?

	@CLIArgument()
	class ArgKeepStdOut(ShortFlag, name="keepstdout"): ...

	@CLIArgument()
	class ArgVHDLLibraryName(ShortTupleFlag, name="lib"): ...

	@CLIArgument()
	class ArgOnFinishMode(ShortTupleFlag, name="onfinish"):
		"""Customize the kernel shutdown behavior at the end of simulation; Valid modes: ask, stop, exit, final (Default: ask)."""

	@CLIArgument()
	class SwitchTopLevel(StringArgument):
		"""The top-level for simulation."""
