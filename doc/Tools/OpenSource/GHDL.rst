GHDL
####

Arguments
*********

.. todo:: Extract the following table from source code by scanning for CLIArgument attributes.

+-----------------+-----------------------------------+----------------------------------------------+
| **GHDL Option** | **Argument Class**                | **Description**                              |
+-----------------+-----------------------------------+----------------------------------------------+
| ``help``        | ``GHDL.CommandHelp``              | Print help page(s).                          |
+-----------------+-----------------------------------+----------------------------------------------+
| ``version``     | ``GHDL.CommandVersion``           | Print version information.                   |
+-----------------+-----------------------------------+----------------------------------------------+
| ``syntax``      | ``GHDL.CommandSyntax``            | Check syntax.                                |
+-----------------+-----------------------------------+----------------------------------------------+
| ``elab-order``  | ``GHDL.CommandElaborationOrder``  | Display (elaboration) ordered source files.  |
+-----------------+-----------------------------------+----------------------------------------------+
| ``analyze``     | ``GHDL.CommandAnalyze``           | Analyze VHDL source file(s).                 |
+-----------------+-----------------------------------+----------------------------------------------+
| ``elaborate``   | ``GHDL.CommandElaborate``         | Elaborate design.                            |
+-----------------+-----------------------------------+----------------------------------------------+
| ``elab-run``    | ``GHDL.CommandElaborationAndRun`` | Elaborate and simulate design.               |
+-----------------+-----------------------------------+----------------------------------------------+
| ``run``         | ``GHDL.CommandRun``               | Simulate design.                             |
+-----------------+-----------------------------------+----------------------------------------------+


Derive Variants
***************

.. code-block:: Python

   def GetGHDLAsAnalyzer(self, std: VHDLVersion = None, ieee: str = None):
     ...

   def GetGHDLAsElaborator(self, std: VHDLVersion = None, ieee: str = None):
     ...

   def GetGHDLAsSimulator(self, std: VHDLVersion = None, ieee: str = None):
     ...
