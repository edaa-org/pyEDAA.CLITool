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
# Copyright 2017-2021 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""This module contains the CLI abstraction layer for `GHDL <https://github.com/ghdl/ghdl>`__."""
from pyVHDLModel import VHDLVersion

from pyTooling.CLIAbstraction            import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument   import (
	CommandArgument,
	ShortFlagArgument, LongFlagArgument,
	ShortValuedFlagArgument, LongValuedFlagArgument
)


class GHDL(Executable):
	_executableNames = {
		"Linux":   "ghdl",
		"Windows": "ghdl.exe"
	}

	# XXX: overwrite __init__ and get backend variant
	# XXX: check for compatible backends

	@CLIOption()
	class FlagHelp(LongFlagArgument, name="help"): ...

	@CLIOption()
	class FlagVersion(LongFlagArgument, name="version"): ...

	@CLIOption()
	class FlagVerbose(ShortFlagArgument, name="v"): ...

	# Analyze options
	@CLIOption()
	class CommandAnalyze(CommandArgument, name="analyze"): ...

	@CLIOption()
	class FlagVHDlStandard(LongValuedFlagArgument, name="std"): ...

	@CLIOption()
	class FlagIEEEFlavor(LongValuedFlagArgument, name="ieee"): ...

	@CLIOption()
	class FlagSynopsys(ShortFlagArgument, name="fsynopsys"): ...

	@CLIOption()
	class FlagRelaxed(ShortFlagArgument, name="frelaxed"): ...

	@CLIOption()
	class FlagExplicit(ShortFlagArgument, name="fexplicit"): ...

	@CLIOption()
	class FlagLibrary(LongValuedFlagArgument, name="work"): ...

	@CLIOption()
	class FlagWorkingDirectory(LongValuedFlagArgument, name="workdir"): ...

	@CLIOption()
	class FlagMultiByteComments(LongFlagArgument, name="mb-comments"): ...

	@CLIOption()
	class FlagSyntesisBindingRule(LongFlagArgument, name="syn-binding"): ...

	@CLIOption()
	class FlagSearchPath(ShortValuedFlagArgument, name="P", pattern="-{0}{1}"): ...

	# TODO: list of files (path list)

	# Elaborate options
	@CLIOption()
	class CommandElaborate(CommandArgument, name="elaborate"): ...

	def _CopyParameters(self, tool: "GHDL") -> None:
		for key in self.__cliParameters__:
			if self._NeedsParameterInitialization(key):
				value = self.__cliParameters__[key].Value
				tool.__cliParameters__[key] = key(value)
			else:
				tool.__cliParameters__[key] = key()

	def _SetParameters(self, tool: "GHDL", std: VHDLVersion=None, ieee: str=None):
		if std is not None:
			tool[self.FlagVHDlStandard] = str(std)

		if ieee is not None:
			tool[self.FlagVHDlStandard] = ieee

	def GetGHDLAsAnalyzer(self, std: VHDLVersion=None, ieee: str=None):
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandAnalyze] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std, ieee)

		return tool

	def GetGHDLAsElaborator(self, std: VHDLVersion=None, ieee: str=None):
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandElaborate] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std, ieee)

		return tool

	def GetGHDLAsSimulator(self, std: VHDLVersion=None, ieee: str=None):
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandRun] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std, ieee)

		return tool
