.. _NEWS:

News
####

See :gh:`pyEDAA.CLITool Release Pages <edaa-org/pyEDAA.CLITool/releases>` for detail release notes on every release.


Version 0.5.0 (2026)
********************

.. topic:: :gh:`v0.5.0 - 29.10.2026 <edaa-org/pyEDAA.CLITool/releases/v0.5.0>`

   .. rubric:: Changes

   * pyTooling 10.1 and pyVHDLModel 0.40 are required; Python 3.11 to 3.15 are supported.
   * ``pyEDAA.CLITool.GHDL`` and ``pyEDAA.CLITool.NVC`` can be imported again on a fresh installation.
   * Executable classes name their executables in the class constant ``_EXECUTABLE_NAMES`` (was ``_executableNames``).
   * The copyright holder is *Electronic Design Automation Abstraction (EDA²)*.

   .. rubric:: Documentation

   * The documentation is built with pyTooling.Sphinx: dependency tables, and report pages per testsuite, source file
     and module.


Version 0.1.0 - 0.4.4 (2022 - 2026)
***********************************

.. only:: html

   July/Dez 2024 - General Updates
   ===============================

.. only:: latex

   .. rubric:: General Updates

* Updated to support pyTooling v8.0.
* Replaced Sphinx theme with ReadTheDocs theme.
* FreeBSD support for GHDL, GTKWave and Docker.
* Reworked documentation.

.. only:: html

   Feb. 2022 - Supporting more Tools
   =================================

.. only:: latex

   .. rubric:: Supporting more Tools

* Added more CLI abstraction.
* Updated to support CLIAbstraction v0.4.0.


.. only:: html

   Jan. 2022 - GHDL, GTKWave, ModelSim
   ===================================

.. only:: latex

   .. rubric:: GHDL, GTKWave, ModelSim

* Added CLI abstraction for GHDL, GTKWave and ModelSim.
* Prepared structure for other vendors and tools.


.. only:: html

   Dec. 2021 - Extracted CLITool from pyIPCMI
   ==========================================

.. only:: latex

   .. rubric:: Extracted CLITool from pyIPCMI

* The EDA tool abstraction has been extracted from `pyIPCMI <https://GitHub.com/Paebbels/pyIPCMI>`__.
