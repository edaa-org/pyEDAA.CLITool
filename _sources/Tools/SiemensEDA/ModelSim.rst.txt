ModelSim
########

.. todo:: Needs documentation.

VHDL Library Tool
*****************

Arguments
=========

.. todo:: Extract the following table from source code by scanning for CLIArgument attributes.

+--------------------+---------------------------------------+----------------------------------------------+
| **vlib Option**    | **Argument Class**                    | **Description**                              |
+--------------------+---------------------------------------+----------------------------------------------+
| ``<lib>``          | ``VHDLLibraryTool.ValueLibraryName``  | Library name to create.                      |
+--------------------+---------------------------------------+----------------------------------------------+


Usage
=====

.. code-block:: Python

   vlib = VHDLLibraryTool()
   vlib[vlib.ValueLibraryName] = "PoC"

   print(vlib.AsArgument())


VHDL Compiler
*************

Arguments
=========

.. todo:: Extract the following table from source code by scanning for CLIArgument attributes.

+--------------------+---------------------------------------+----------------------------------------------+
| **vcom Option**    | **Argument Class**                    | **Description**                              |
+--------------------+---------------------------------------+----------------------------------------------+

.. #| ``<lib>``          | ``VHDLLibraryTool.ValueLibraryName``  | Library name to create.                      |
    +--------------------+---------------------------------------+----------------------------------------------+


Usage
=====

.. code-block:: Python

   vcom = VHDLCompiler()
   # vcom[vcom.ValueLibraryName] = "PoC"

   print(vcom.AsArgument())

.. #
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


(System-)Verilog Compiler
*************************

.. todo:: This tool is not yet wrapped in Python using CLIAbstraction.

Arguments
=========

.. todo:: Extract the following table from source code by scanning for CLIArgument attributes.

+--------------------+---------------------------------------+----------------------------------------------+
| **vlog Option**    | **Argument Class**                    | **Description**                              |
+--------------------+---------------------------------------+----------------------------------------------+

.. #| ``<lib>``          | ``VHDLLibraryTool.ValueLibraryName``  | Library name to create.                      |
    +--------------------+---------------------------------------+----------------------------------------------+


Usage
=====

.. code-block:: Python

   vlog = VerilogCompiler()
   # vlog[vlog.ValueLibraryName] = "PoC"

   print(vlog.AsArgument())


VHDL Simulator
**************

Arguments
=========

.. todo:: Extract the following table from source code by scanning for CLIArgument attributes.

+--------------------+---------------------------------------+----------------------------------------------+
| **vsim Option**    | **Argument Class**                    | **Description**                              |
+--------------------+---------------------------------------+----------------------------------------------+

.. #| ``<lib>``          | ``VHDLLibraryTool.ValueLibraryName``  | Library name to create.                      |
    +--------------------+---------------------------------------+----------------------------------------------+


Usage
=====

.. code-block:: Python

   vsim = VHDLSimulator()
   # vsim[vsim.ValueLibraryName] = "PoC"

   print(vsim.AsArgument())

.. #
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
