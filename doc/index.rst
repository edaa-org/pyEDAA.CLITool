.. include:: shields.inc

.. image:: _static/logo.svg
   :height: 90 px
   :align: center
   :target: https://GitHub.com/edaa-org/pyEDAA.CLITool

.. raw:: html

    <br>

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:CLITool-github| |SHIELD:svg:CLITool-src-license| |SHIELD:svg:CLITool-ghp-doc| |SHIELD:svg:CLITool-doc-license| |SHIELD:svg:CLITool-gitter|
   |  |SHIELD:svg:CLITool-pypi-tag| |SHIELD:svg:CLITool-pypi-status| |SHIELD:svg:CLITool-pypi-python|
   |  |SHIELD:svg:CLITool-gha-test| |SHIELD:svg:CLITool-lib-status| |SHIELD:svg:CLITool-codacy-quality| |SHIELD:svg:CLITool-codacy-coverage| |SHIELD:svg:CLITool-codecov-coverage|

.. Disabled shields: |SHIELD:svg:CLITool-lib-dep| |SHIELD:svg:CLITool-req-status| |SHIELD:svg:CLITool-lib-rank|

.. only:: latex

   |SHIELD:png:CLITool-github| |SHIELD:png:CLITool-src-license| |SHIELD:png:CLITool-ghp-doc| |SHIELD:png:CLITool-doc-license| |SHIELD:svg:CLITool-gitter|
   |SHIELD:png:CLITool-pypi-tag| |SHIELD:png:CLITool-pypi-status| |SHIELD:png:CLITool-pypi-python|
   |SHIELD:png:CLITool-gha-test| |SHIELD:png:CLITool-lib-status| |SHIELD:png:CLITool-codacy-quality| |SHIELD:png:CLITool-codacy-coverage| |SHIELD:png:CLITool-codecov-coverage|

.. Disabled shields: |SHIELD:png:CLITool-lib-dep| |SHIELD:png:CLITool-req-status| |SHIELD:png:CLITool-lib-rank|


The pyEDAA.CLITool Documentation
################################

Unified interfaces to execute EDA tools via CLI from Python, agnostic to any specific configuration format/object.


.. _GOALS:

Main Goals
**********

* Provide a pythonic solution to construct command line calls for EDA tools based on `pyTooling.CLIAbstraction <https://github.com/pyTooling/pyTooling>`__
* Launch CLI tools and connect to STDIN, STDOUT, STDERR for realtime output post-processing.


.. _FEATURES:

Features
********

* Support multiple native platforms: Linux, macOS, Windows.
* Support nested platforms like MSYS2 with MinGW32, MinGW64, UCRT64, Clang64, ...
* Find CLI programs either in ``PATH`` or specify an exact installation location.
* Generate CLI options in correct order.
* Generate correctly escaped CLI options.


.. _CONSUMERS:

Consumers
*********

This layer is used by:

* 🚧 `pyEDAA.Workflow <https://github.com/edaa-org/pyEDAA.Workflow>`__
* 🚧 `pyEDAA.Launcher <https://github.com/edaa-org/pyEDAA.Launcher>`__
* 🚧 `Open Source Verification Bundle (OSVB) <https://umarcor.github.io/osvb>`__


.. _NEWS:

News
****

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


.. _CONTRIBUTORS:

Contributors
************

* `Patrick Lehmann <https://GitHub.com/Paebbels>`__ (Maintainer)
* `Unai Martinez-Corral <https://GitHub.com/umarcor/>`__
* `and more... <https://GitHub.com/edaa-org/pyEDAA.CLITool/graphs/contributors>`__


.. _LICENSE:

License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


.. toctree::
   :hidden:

   Used as a layer of EDA² ➚ <https://edaa-org.github.io/>

.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency


.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Main Documentation
   :hidden:

   Tutorial
   Tools/index

.. raw:: latex

   \part{References and Reports}

.. toctree::
   :caption: References and Reports
   :hidden:

   pyEDAA.CLITool/pyEDAA.CLITool
   unittests/index
   coverage/index
   Doc. Coverage Report <DocCoverage>
   Static Type Check Report ➚ <typing/index>

.. Coverage Report ➚ <coverage/index>
   Static Type Check Report ➚ <typing/index>

.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   License
   Doc-License
   Glossary
   genindex
   Python Module Index <modindex>
   TODO
