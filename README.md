<p align="center">
  <a title="edaa-org.github.io/pyEDAA.CLITool" href="https://edaa-org.github.io/pyEDAA.CLITool"><img height="80px" src="doc/_static/logo.svg"/></a>
</p>

[![Sourcecode on GitHub](https://img.shields.io/badge/pyEDAA-CLITool-ffca28.svg?longCache=true&style=flat-square&logo=github&longCache=true&logo=GitHub&labelColor=ff8f00)](https://GitHub.com/edaa-org/pyEDAA.CLITool)
[![Sourcecode License](https://img.shields.io/pypi/l/pyEDAA.CLITool?longCache=true&style=flat-square&logo=Apache&label=code)](LICENSE.md)
[![Documentation](https://img.shields.io/website?longCache=true&style=flat-square&label=edaa-org.github.io%2FpyEDAA.CLITool&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2Fedaa-org.github.io%2FpyEDAA.CLITool%2Findex.html)](https://edaa-org.github.io/pyEDAA.CLITool/)
[![Documentation License](https://img.shields.io/badge/doc-CC--BY%204.0-green?longCache=true&style=flat-square&logo=CreativeCommons&logoColor=fff)](LICENSE.md)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef)](https://gitter.im/hdl/community)  
[![PyPI](https://img.shields.io/pypi/v/pyEDAA.CLITool?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyEDAA.CLITool/)
![PyPI - Status](https://img.shields.io/pypi/status/pyEDAA.CLITool?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyEDAA.CLITool?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/actions/workflow/status/edaa-org/pyEDAA.CLITool/Pipeline.yml?longCache=true&style=flat-square&label=Build%20and%20test&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/edaa-org/pyEDAA.CLITool/actions/workflows/Pipeline.yml)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyEDAA.CLITool?longCache=true&style=flat-square&logo=Libraries.io&logoColor=fff)](https://libraries.io/github/edaa-org/pyEDAA.CLITool)
[![Codacy - Quality](https://img.shields.io/codacy/grade/7cc5334a04924f77ae75bbffbf48ff98?longCache=true&style=flat-square&logo=Codacy)](https://www.codacy.com/gh/edaa-org/pyEDAA.CLITool)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/7cc5334a04924f77ae75bbffbf48ff98?longCache=true&style=flat-square&logo=Codacy)](https://www.codacy.com/gh/edaa-org/pyEDAA.CLITool)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/edaa-org/pyEDAA.CLITool?longCache=true&style=flat-square&logo=Codecov)](https://codecov.io/gh/edaa-org/pyEDAA.CLITool)

<!--
[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyEDAA.CLITool?longCache=true&style=flat-square&logo=GitHub)](https://github.com/edaa-org/pyEDAA.CLITool/network/dependents)
[![Requires.io](https://img.shields.io/requires/github/edaa-org/pyEDAA.CLITool?longCache=true&style=flat-square)](https://requires.io/github/edaa-org/pyEDAA.CLITool/requirements/?branch=main)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyEDAA.CLITool)](https://libraries.io/github/edaa-org/pyEDAA.CLITool/sourcerank)  
-->


Provide unified interfaces to execute EDA tools via CLI from Python, agnostic to any specific configuration format/object.


# Main Goals

* Provide a pythonic solution to construct command line calls for EDA tools based on [pyTooling.CLIAbstraction](https://github.com/pyTooling/pyTooling.CLIAbstraction)
* Launch CLI tools and connect to STDIn, STDOUT, STDERR for realtime output post-processing.


# Features

* Support multiple native platforms: Linux, macOS, Windows.
* Support nested platforms like MSYS2 with MinGW32, MinGW64, URCT64, Clang64, ...
* Find CLI programs either in `PATH` or specify an exact installation location.
* Generate CLI options in correct order.
* Generate correctly escaped CLI options.


# Supported Tools

* Aldec
  * 🚧 Active-HDL
  * 🚧 Riviera-PRO
* Altera
  * 🚧 Quartus
  * 🚫 ModelSim Altera (Student) Edition
* Cadence
  * 🙋 need a list of tools
* IntelFPGA
  * 🚧 Quartus
  * 🚫 ModelSim Altera (Student) Edition
* Lattice
  * 🚧 Diamond
  * 🚫 Active-HDL Lattice Edition
  * 🚫 ModelSim Lattice Edition
* MentorGraphics
  * ✅ ModelSim DE/SE/PE
  * 🚫 QuestaSim
* SiemensEDA
  * 🚫 ModelSim DE/SE/PE
  * 🚫 QuestaSim
* Synopsys
  * 🙋 need a list of tools
* Xilinx
  * 🚧 ISE
  * 🚧 Vivado
  * 🚫 Vivado-SDK
  * 🚫 Vitis
* System Tools
  * ✅ Git
* Open Source
  * ✅ GHDL
  * ✅ GTKWave
* Yosys
  * 🙋 need a list of tools

**Legend:**  
✅ &rarr; implemented and tested  
🚧 &rarr; under test  
🚫 &rarr; planned but not yet implemented &rArr; accepting PRs  
🙋 &rarr; need help

# Examples

```python
from pyEDAA.CLITool.GHDL import GHDL

tool = GHDL()
tool[tool.CommandAnalyze] = True
tool[tool.FlagVHDLStandard] = "08"
tool[tool.FlagSynopsys] = True
tool[tool.FlagRelaxed] = True
tool[tool.FlagExplicit] = True
tool[tool.FlagMultiByteComments] = True
tool[tool.FlagLibrary] = "lib_Test"

print(f"Calling GHDL: {tool}")
# Calling GHDL: "ghdl" "analyze" "--std=08" "-fsynopsys" "-frelaxed" "-fexplicit" "--work=lib_Test" "--mb-comments"
```

# Consumers

This layer is used by:

* 🚧 [pyEDAA.Workflow](https://github.com/edaa-org/pyEDAA.Workflow)
* 🚧 [pyEDAA.Launcher](https://github.com/edaa-org/pyEDAA.Launcher)
* 🚧 [Open Source Verification Bundle (OSVB)](https://umarcor.github.io/osvb)


# References

* [docs.siliconcompiler.com: Tools directory](https://docs.siliconcompiler.com/en/latest/reference_manual/tools.html)
* GHDL:
  * [Paebbels/pyIPCMI: pyIPCMI/Simulator/GHDLSimulator.py](https://github.com/Paebbels/pyIPCMI/blob/0f91e26f989ca025c9380ff808d1e532614b9593/pyIPCMI/Simulator/GHDLSimulator.py#L49)
  * [VUnit/vunit: vunit/sim_if/ghdl.py](https://github.com/VUnit/vunit/blob/f344c8b5642d7aa13db2e16f6fc7151585ca96d0/vunit/sim_if/ghdl.py#L29)
  * [olofk/edalize: edalize/ghdl.py](https://github.com/olofk/edalize/blob/322773113716fa29fddd800c2e0992bb5dd2ed79/edalize/ghdl.py#L13)
  * [im-tomu/fomu-workshop: hdl/mixed/blink/Makefile](https://github.com/im-tomu/fomu-workshop/blob/6e6318d820271750a99c8e419ee1b9abd9aa6b81/hdl/mixed/blink/Makefile#L45-L51)
  * [PyFPGA/pyfpga: fpga/tool/openflow.py](https://github.com/PyFPGA/pyfpga/blob/507631b780a4ab658304bfcdcec133a0e9b8a769/fpga/tool/openflow.py#L28)
  * [XedaHQ/xeda: xeda/flows/ghdl/__init__.py](https://github.com/XedaHQ/xeda/blob/e5bea8663a9001d0e98f6b7a91575e13fba06493/xeda/flows/ghdl/__init__.py#L8)
  * [cocotb/cocotb: cocotb/runner.py](https://github.com/cocotb/cocotb/blob/fa7a826cc855d783b7fbc81444d4e6b9edc487b9/cocotb/runner.py#L444) ([cocotb/cocotb#2634](https://github.com/cocotb/cocotb/pull/2634))
  * [stnolting/neorv32: tasks/examples.py](https://github.com/stnolting/neorv32/blob/6dd30e78101cd08310fe02b8818050745dd3a6ad/tasks/examples.py#L13) ([stnolting/neorv32#110](https://github.com/stnolting/neorv32/pull/110))
  * [ghdl/ghdl: scripts/vendors/shared.sh](https://github.com/ghdl/ghdl/blob/7e41be2dabf79b21f3d0be210e3d01d541a7e82c/scripts/vendors/shared.sh#L132)
    * [ghdl/ghdl: scripts/vendors/shared.psm1](https://github.com/ghdl/ghdl/blob/7e41be2dabf79b21f3d0be210e3d01d541a7e82c/scripts/vendors/shared.psm1#L261)
  * [OSVVM/OSVVM-Scripts: VendorScripts_GHDL.tcl](https://github.com/OSVVM/OSVVM-Scripts/blob/3f52f725603166b4bfd6c862629f1dad363fd2f7/VendorScripts_GHDL.tcl#L143)

# Contributors

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)
* [Unai Martinez-Corral](https://github.com/umarcor)
* [and more...](https://github.com/edaa-org/pyEDAA.CLITool/graphs/contributors)


# License

This Python package (source code) is licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).

---
SPDX-License-Identifier: Apache-2.0
