from enum import Enum

from flags import Flags
from pyTooling.Decorators import export

from pyEDAA.CLITool import ToolMixIn
from pyTooling.CLIAbstraction            import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument import (
	ShortFlagArgument, LongFlagArgument,
	ShortValuedFlagArgument, LongValuedFlagArgument,
	StringArgument, OptionalValuedFlagArgument, ShortTupleArgument
)


@export
class VHDLLibraryTool(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vlib",
		"Windows": "vlib.exe"
	}

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

	class FlagTime(ShortFlagArgument, name="time"):
		"""Print the compilation wall clock time."""

	class FlagExplicit(ShortFlagArgument, name="explicit"): ...

	class FlagQuietMode(ShortFlagArgument, name="quiet"):
		"""Do not report 'Loading...' messages."""

	class SwitchModelSimIniFile(ShortTupleArgument, name="modelsimini"): ...

	class FlagRangeCheck(ShortFlagArgument, name="rangecheck"): ...

	class SwitchCoverage(OptionalModelSimPlusArgument, name="cover"): ...

	class FlagEnableFocusedExpressionCoverage(ShortFlagArgument, name="coverfec"): ...

	class FlagDisableFocusedExpressionCoverage(ShortFlagArgument, name="nocoverfec"): ...

	class FlagEnableRapidExpressionCoverage(ShortFlagArgument, name="coverrec"): ...

	class FlagDisableRapidExpressionCoverage(ShortFlagArgument, name="nocoverrec"): ...

	class FlagEnableRecognitionOfImplicitFSMResetTransitions(ShortFlagArgument, name="fsmresettrans"): ...

	class FlagDisableRecognitionOfImplicitFSMResetTransitions(ShortFlagArgument, name="nofsmresettrans"): ...

	class FlagEnableRecognitionOfSingleBitFSMState(ShortFlagArgument, name="fsmsingle"): ...

	class FlagDisableRecognitionOfSingleBitFSMState(ShortFlagArgument, name="nofsmsingle"): ...

	class FlagEnableRecognitionOfImplicitFSMTransitions(ShortFlagArgument, name="fsmimplicittrans"): ...

	class FlagDisableRecognitionOfImplicitFSMTransitions(ShortFlagArgument, name="nofsmimplicittrans"): ...

	class SwitchFSMVerbosityLevel(OptionalModelSimMinusArgument, name="fsmverbose"): ...

	class FlagReportAsNote(ShortTupleArgument, name="note"): ...

	class FlagReportAsError(ShortTupleArgument, name="error"): ...

	class FlagReportAsWarning(ShortTupleArgument, name="warning"): ...

	class FlagReportAsFatal(ShortTupleArgument, name="fatal"): ...

	class FlagRelaxLanguageChecks(ShortFlagArgument, name="permissive"): ...

	class FlagForceLanguageChecks(ShortFlagArgument, name="pedanticerrors"): ...

	class SwitchVHDLVersion(StringArgument, pattern="-{0}"): ...

	class ArgLogFile(ShortTupleArgument, name="l"): ...			# what's the difference to -logfile ?

	class SwitchVHDLLibrary(ShortTupleArgument, name="work"): ...

	class ArgSourceFile(PathArgument): ...


class VHDLSimulator(Executable, ToolMixIn):
	_executableNames = {
		"Linux":   "vsim",
		"Windows": "vsim.exe"
	}

	class FlagQuietMode(ShortFlagArgument, name="quiet"):
		"""Run simulation in quiet mode. (Don't show 'Loading...' messages."""

	class FlagBatchMode(ShortFlagArgument, name="batch"):
		"""Run simulation in batch mode."""

	class FlagGuiMode(ShortFlagArgument, name="gui"):
		"""Run simulation in GUI mode."""

	class SwitchBatchCommand(ShortTupleArgument, name="do"):
		"""Specify a Tcl batch script for the batch mode."""

	class FlagCommandLineMode(ShortFlagArgument, name="c"):
		"""Run simulation in command line mode."""

	class SwitchModelSimIniFile(ShortTupleArgument, name="modelsimini"):
		"""Specify the used 'modelsim.ini' file."""

	class FlagEnableOptimization(ShortFlagArgument, name="vopt"):
		"""Enabled optimization while elaborating the design."""

	class FlagDisableOptimization(ShortFlagArgument, name="novopt"):
		"""Disabled optimization while elaborating the design."""

	class FlagEnableOptimizationVerbosity(ShortFlagArgument, name="vopt_verbose"):
		"""Enabled optimization while elaborating the design."""

	class FlagEnableKeepAssertionCountsForCoverage(ShortFlagArgument, name="assertcover"): ...

	class FlagDisableKeepAssertionCountsForCoverage(ShortFlagArgument, name="noassertcover"): ...

	class FlagEnableCoverage(ShortFlagArgument, name="coverage"): ...

	class FlagDisableCoverage(ShortFlagArgument, name="nocoverage"): ...

	class FlagEnablePSL(ShortFlagArgument, name="psl"): ...

	class FlagDisablePSL(ShortFlagArgument, name="nopsl"): ...

	class FlagEnableFSMDebugging(ShortFlagArgument, name="fsmdebug"): ...

	class FlagReportAsNote(ShortTupleArgument, name="note"): ...

	class FlagReportAsError(ShortTupleArgument, name="error"): ...

	class FlagReportAsWarning(ShortTupleArgument, name="warning"): ...

	class FlagReportAsFatal(ShortTupleArgument, name="fatal"): ...

	class FlagRelaxLanguageChecks(ShortFlagArgument, name="permissive"): ...

	class FlagForceLanguageChecks(ShortFlagArgument, name="pedanticerrors"): ...

	class SwitchTimeResolution(ShortTupleArgument, name="t"):
		"""Set simulation time resolution."""
		# -t [1|10|100]fs|ps|ns|us|ms|sec  Time resolution limit

	class ArgLogFile(ShortTupleArgument, name="l"): ...
		# what's the difference to -logfile ?

	class ArgKeepStdOut(ShortFlagArgument, name="keepstdout"): ...

	class ArgVHDLLibraryName(ShortTupleArgument, name="lib"): ...

	class ArgOnFinishMode(ShortTupleArgument, name="onfinish"):
		"""Customize the kernel shutdown behavior at the end of simulation; Valid modes: ask, stop, exit, final (Default: ask)."""

	class SwitchTopLevel(StringArgument):
		"""The top-level for simulation."""
