Riviera-PRO
###########

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
