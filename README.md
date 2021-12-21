<p align="center">
  <a title="edaa-org.github.io/pyEDAA.CLITool" href="https://edaa-org.github.io/pyEDAA.CLITool"><img height="80px" src="doc/_static/logo.svg"/></a>
</p>

[![Sourcecode on GitHub](https://img.shields.io/badge/pyEDAA-CLITool-ffca28.svg?longCache=true&style=flat-square&logo=GitHub&labelColor=ff8f00)](https://GitHub.com/edaa-org/pyEDAA.CLITool)
[![Documentation](https://img.shields.io/website?longCache=true&style=flat-square&label=edaa-org.github.io%2FpyEDAA.CLITool&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2Fedaa-org.github.io%2FpyEDAA.CLITool%2Findex.html)](https://edaa-org.github.io/pyEDAA.CLITool/)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef)](https://gitter.im/hdl/community)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/edaa-org/pyEDAA.CLITool/Pipeline/main?longCache=true&style=flat-square&label=Build%20and%20Test&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/edaa-org/pyEDAA.CLITool/actions/workflows/Pipeline.yml)

<!--
[![Sourcecode License](https://img.shields.io/pypi/l/pyEDAA.CLITool?longCache=true&style=flat-square&logo=Apache&label=code)](LICENSE.md)
[![Documentation License](https://img.shields.io/badge/doc-CC--BY%204.0-green?longCache=true&style=flat-square&logo=CreativeCommons&logoColor=fff)](LICENSE.md)

[![PyPI](https://img.shields.io/pypi/v/pyEDAA.CLITool?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyEDAA.CLITool/)
![PyPI - Status](https://img.shields.io/pypi/status/pyEDAA.CLITool?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyEDAA.CLITool?longCache=true&style=flat-square&logo=PyPI&logoColor=FBE072)

[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyEDAA.CLITool?longCache=true&style=flat-square&logo=Libraries.io&logoColor=fff)](https://libraries.io/github/edaa-org/pyEDAA.CLITool)
[![Codacy - Quality](https://img.shields.io/codacy/grade/39d312bf98244961975559f141c3e000?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pyEDAA.CLITool)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/39d312bf98244961975559f141c3e000?longCache=true&style=flat-square&logo=Codacy)](https://app.codacy.com/gh/edaa-org/pyEDAA.CLITool)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/edaa-org/pyEDAA.CLITool?longCache=true&style=flat-square&logo=Codecov)](https://codecov.io/gh/edaa-org/pyEDAA.CLITool)

[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyEDAA.CLITool?longCache=true&style=flat-square&logo=GitHub)](https://GitHub.com/edaa-org/pyEDAA.CLITool/network/dependents)
[![Requires.io](https://img.shields.io/requires/github/edaa-org/pyEDAA.CLITool?longCache=true&style=flat-square)](https://requires.io/github/EDAA-ORG/pyEDAA.CLITool/requirements/?branch=main)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyEDAA.CLITool?longCache=true&style=flat-square)](https://libraries.io/github/edaa-org/pyEDAA.CLITool/sourcerank)
-->

<p align="center">
  <a title="edaa-org.github.io/pyEDAA.CLITool" href="https://edaa-org.github.io/pyEDAA.CLITool"><img height="275px" src="doc/_static/work-in-progress.png"/></a>
</p>


# Main Goals

Provide unified interfaces to execute EDA tools via CLI from Python, agnostic to any specific configuration format/object.


# Use Cases

* *tbd*


# Examples

```python
print(some.python.code.here())
```


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
