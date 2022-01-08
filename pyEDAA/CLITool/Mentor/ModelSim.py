from enum import Enum

from flags import Flags
from pyTooling.Decorators import export

from pyEDAA.CLITool import ToolMixIn
from pyTooling.CLIAbstraction            import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument import (
	ShortFlagArgument,
	StringArgument, OptionalValuedFlagArgument, ShortTupleArgument
)


@export
class VHDLLibraryTool(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vlib",
		"Windows": "vlib.exe"
	}

	@CLIOption
	class ValueLibraryName(StringArgument): ...


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

	def __str__(self):
		return "".join([i.value for i in self])


@export
class VHDLCompilerFSMVerbosityLevel(Enum):
	Default =         ""
	Basic =           "b"
	TransitionTable = "t"
	AnyWarning =      "w"

	def __str__(self):
		return self.value


@export
class OptionalModelSimMinusArgument(OptionalValuedFlagArgument, pattern="-{0}", patternWithValue="-{0} {1}"):
	pass


@export
class OptionalModelSimPlusArgument(OptionalValuedFlagArgument, pattern="-{0}", patternWithValue="+{0} {1}"):
	pass


@export
class VHDLCompiler(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vcom",
		"Windows": "vcom.exe"
	}

	@CLIOption
	class FlagTime(ShortFlagArgument, name="time"):
		"""Print the compilation wall clock time."""

	@CLIOption
	class FlagExplicit(ShortFlagArgument, name="explicit"): ...

	@CLIOption
	class FlagQuietMode(ShortFlagArgument, name="quiet"):
		"""Do not report 'Loading...' messages."""

	@CLIOption
	class SwitchModelSimIniFile(ShortTupleArgument, name="modelsimini"): ...

	@CLIOption
	class FlagRangeCheck(ShortFlagArgument, name="rangecheck"): ...

	@CLIOption
	class SwitchCoverage(OptionalModelSimPlusArgument, name="cover"): ...

	@CLIOption
	class FlagEnableFocusedExpressionCoverage(ShortFlagArgument, name="coverfec"): ...

	@CLIOption
	class FlagDisableFocusedExpressionCoverage(ShortFlagArgument, name="nocoverfec"): ...

	@CLIOption
	class FlagEnableRapidExpressionCoverage(ShortFlagArgument, name="coverrec"): ...

	@CLIOption
	class FlagDisableRapidExpressionCoverage(ShortFlagArgument, name="nocoverrec"): ...

	@CLIOption
	class FlagEnableRecognitionOfImplicitFSMResetTransitions(ShortFlagArgument, name="fsmresettrans"): ...

	@CLIOption
	class FlagDisableRecognitionOfImplicitFSMResetTransitions(ShortFlagArgument, name="nofsmresettrans"): ...

	@CLIOption
	class FlagEnableRecognitionOfSingleBitFSMState(ShortFlagArgument, name="fsmsingle"): ...

	@CLIOption
	class FlagDisableRecognitionOfSingleBitFSMState(ShortFlagArgument, name="nofsmsingle"): ...

	@CLIOption
	class FlagEnableRecognitionOfImplicitFSMTransitions(ShortFlagArgument, name="fsmimplicittrans"): ...

	@CLIOption
	class FlagDisableRecognitionOfImplicitFSMTransitions(ShortFlagArgument, name="nofsmimplicittrans"): ...

	@CLIOption
	class SwitchFSMVerbosityLevel(OptionalModelSimMinusArgument, name="fsmverbose"): ...

	@CLIOption
	class FlagReportAsNote(ShortTupleArgument, name="note"): ...

	@CLIOption
	class FlagReportAsError(ShortTupleArgument, name="error"): ...

	@CLIOption
	class FlagReportAsWarning(ShortTupleArgument, name="warning"): ...

	@CLIOption
	class FlagReportAsFatal(ShortTupleArgument, name="fatal"): ...

	@CLIOption
	class FlagRelaxLanguageChecks(ShortFlagArgument, name="permissive"): ...

	@CLIOption
	class FlagForceLanguageChecks(ShortFlagArgument, name="pedanticerrors"): ...

	@CLIOption
	class SwitchVHDLVersion(StringArgument, pattern="-{0}"): ...

	@CLIOption
	class ArgLogFile(ShortTupleArgument, name="l"): ...			# what's the difference to -logfile ?

	@CLIOption
	class SwitchVHDLLibrary(ShortTupleArgument, name="work"): ...

	# @CLIOption
	# class ArgSourceFile(PathArgument): ...


class VHDLSimulator(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vsim",
		"Windows": "vsim.exe"
	}

	@CLIOption
	class FlagQuietMode(ShortFlagArgument, name="quiet"):
		"""Run simulation in quiet mode. (Don't show 'Loading...' messages."""

	@CLIOption
	class FlagBatchMode(ShortFlagArgument, name="batch"):
		"""Run simulation in batch mode."""

	@CLIOption
	class FlagGuiMode(ShortFlagArgument, name="gui"):
		"""Run simulation in GUI mode."""

	@CLIOption
	class SwitchBatchCommand(ShortTupleArgument, name="do"):
		"""Specify a Tcl batch script for the batch mode."""

	@CLIOption
	class FlagCommandLineMode(ShortFlagArgument, name="c"):
		"""Run simulation in command line mode."""

	@CLIOption
	class SwitchModelSimIniFile(ShortTupleArgument, name="modelsimini"):
		"""Specify the used 'modelsim.ini' file."""

	@CLIOption
	class FlagEnableOptimization(ShortFlagArgument, name="vopt"):
		"""Enabled optimization while elaborating the design."""

	@CLIOption
	class FlagDisableOptimization(ShortFlagArgument, name="novopt"):
		"""Disabled optimization while elaborating the design."""

	@CLIOption
	class FlagEnableOptimizationVerbosity(ShortFlagArgument, name="vopt_verbose"):
		"""Enabled optimization while elaborating the design."""

	@CLIOption
	class FlagEnableKeepAssertionCountsForCoverage(ShortFlagArgument, name="assertcover"): ...

	@CLIOption
	class FlagDisableKeepAssertionCountsForCoverage(ShortFlagArgument, name="noassertcover"): ...

	@CLIOption
	class FlagEnableCoverage(ShortFlagArgument, name="coverage"): ...

	@CLIOption
	class FlagDisableCoverage(ShortFlagArgument, name="nocoverage"): ...

	@CLIOption
	class FlagEnablePSL(ShortFlagArgument, name="psl"): ...

	@CLIOption
	class FlagDisablePSL(ShortFlagArgument, name="nopsl"): ...

	@CLIOption
	class FlagEnableFSMDebugging(ShortFlagArgument, name="fsmdebug"): ...

	@CLIOption
	class FlagReportAsNote(ShortTupleArgument, name="note"): ...

	@CLIOption
	class FlagReportAsError(ShortTupleArgument, name="error"): ...

	@CLIOption
	class FlagReportAsWarning(ShortTupleArgument, name="warning"): ...

	@CLIOption
	class FlagReportAsFatal(ShortTupleArgument, name="fatal"): ...

	@CLIOption
	class FlagRelaxLanguageChecks(ShortFlagArgument, name="permissive"): ...

	@CLIOption
	class FlagForceLanguageChecks(ShortFlagArgument, name="pedanticerrors"): ...

	@CLIOption
	class SwitchTimeResolution(ShortTupleArgument, name="t"):
		"""Set simulation time resolution."""
		# -t [1|10|100]fs|ps|ns|us|ms|sec  Time resolution limit

	@CLIOption
	class ArgLogFile(ShortTupleArgument, name="l"): ...
		# what's the difference to -logfile ?

	@CLIOption
	class ArgKeepStdOut(ShortFlagArgument, name="keepstdout"): ...

	@CLIOption
	class ArgVHDLLibraryName(ShortTupleArgument, name="lib"): ...

	@CLIOption
	class ArgOnFinishMode(ShortTupleArgument, name="onfinish"):
		"""Customize the kernel shutdown behavior at the end of simulation; Valid modes: ask, stop, exit, final (Default: ask)."""

	@CLIOption
	class SwitchTopLevel(StringArgument):
		"""The top-level for simulation."""