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
# Copyright 2025-2026 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""This module contains the CLI abstraction layer for `NVC <https://github.com/nickg/nvc>`__."""
from re                    import search as re_search
from typing                import Union, Iterable, Optional as Nullable

from pyTooling.Decorators  import export
from pyTooling.MetaClasses import ExtendedType
from pyVHDLModel           import VHDLVersion

from pyTooling.CLIAbstraction                 import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument        import PathListArgument, StringArgument
from pyTooling.CLIAbstraction.Command         import LongCommand
from pyTooling.CLIAbstraction.Flag            import ShortFlag, LongFlag
from pyTooling.CLIAbstraction.BooleanFlag     import LongBooleanFlag
from pyTooling.CLIAbstraction.ValuedFlag      import ShortValuedFlag, LongValuedFlag
from pyTooling.CLIAbstraction.ValuedTupleFlag import LongTupleFlag, ShortTupleFlag
from pyTooling.CLIAbstraction.KeyValueFlag    import ShortKeyValueFlag, LongKeyValueFlag

from pyEDAA.CLITool                           import CLIToolException


@export
class NVCVersion(metaclass=ExtendedType, slots=True):
	"""

  .. code-block::

	   nvc 1.18.2 (1.18.2.r0.g8893318a) (Using LLVM 21.1.5)
     Copyright (C) 2011-2025  Nick Gasson
     This program comes with ABSOLUTELY NO WARRANTY. This is free software, and
     you are welcome to redistribute it under certain conditions. See the GNU
     General Public Licence for details.
	"""
	_major: int
	_minor: int
	_micro: int
	# _dev:   bool
	_commitsSinceLastTag: int
	_gitHash: str
	_backend: str

	VERSION_LINE_PATTERN = (
		r"nvc"
		r"\s(?P<Major>\d+)\.(?P<Minor>\d+)\.(?P<Micro>\d+)(?:-(?P<Suffix>dev|rc\d+))?"
		r"\s\((?:"
			r"(?:"
				r"(?P<major2>\d+)\.(?P<minor2>\d+)\.(?P<micro2>\d+)\.(?:r(?P<cslt>\d+))\.(?:g(?P<Hash>[0-9a-f]+))(?:\.(?P<Dirty>dirty))?"
			r")|(?:"
				r"(?P<Hash2>[0-9a-f]{7})"
			r")"
		r")\)"
		r"\s\(Using (?P<Backend>\w+) (?P<BackendMajor>\d+)\.(?P<BackendMinor>\d+)\.(?P<BackendMicro>\d+)\)"
	)

	def __init__(self, versionLine: str) -> None:
		match = re_search("^" + self.VERSION_LINE_PATTERN + "$", versionLine)
		if match is None:
			raise CLIToolException(f"Unknown NVC version string '{versionLine}'.")

		self._major = int(match["Major"])
		self._minor = int(match["Minor"])
		self._micro = int(match["Micro"])
		# if (suffix := match["Suffix"]) is not None:
		# 	self._dev = suffix == "dev"
		# else:
		# 	self._dev = False
		if (cslt := match["cslt"]) is not None:
			self._commitsSinceLastTag = int(cslt)
		else:
			self._commitsSinceLastTag = 0
		self._gitHash = match["Hash"] if match["Hash"] is not None else match["Hash2"]
		self._backend = match["Backend"]

	@property
	def Major(self) -> int:
		return self._major

	@property
	def Minor(self) -> int:
		return self._minor

	@property
	def Micro(self) -> int:
		return self._micro

	@property
	def CommitsSinceLastTag(self) -> int:
		return self._commitsSinceLastTag

	@property
	def GitHash(self) -> str:
		return self._gitHash

	@property
	def Dirty(self) -> bool:
		return self._dirty

	@property
	def Backend(self) -> str:
		return self._backend

	def __str__(self) -> str:
		# dev = f"-dev" if self._dev else ""
		return f"{self._major}.{self._minor}.{self._micro}"  # {dev}"

	def __repr__(self) -> str:
		return f"{self.__str__()} (Backend: {self._backend}; Git: {self._gitHash})"


@export
class NVC(Executable):
	_executableNames = {
		"Darwin":  "nvc",
		"FreeBSD": "nvc",
		"Linux":   "nvc",
		"Windows": "nvc.exe"
	}

	@CLIArgument()
	class CommandHelp(LongCommand, name="help"):
		"""Display usage summary."""

	@CLIArgument()
	class CommandVersion(LongCommand, name="version"):
		"""Display version and copyright information."""

	@CLIArgument()
	class FlagSimulationHeapSize(ShortTupleFlag, name="H"):
		"""
		Set the maximum size in bytes of the simulation heap. This area of memory is used for temporary allocations during
		process execution and dynamic allocations by the VHDL ‘new’ operator. The size parameter takes an optional k, m, or
		g suffix to indicate kilobytes, megabytes, and gigabytes respectively. The default size is 16 megabytes.
		"""

	@CLIArgument()
	class FlagIEEEWarnings(LongValuedFlag, name="ieee-warnings"):
		"""
		Enable or disable warning messages from the standard IEEE packages. The off-at-0 option disables warnings in the
		first time step only. The default is warnings enabled.
		"""

	@CLIArgument()
	class FlagIgnoreTime(LongFlag, name="ignore-time"):
		"""
		Do not check the timestamps of source files when the corresponding design unit is loaded from a library.
		"""

	@CLIArgument()
	class FlagLibrarySearchPath(ShortTupleFlag, name="L"):
		"""
		Add path to the list of directories to search for libraries. See the LIBRARIES section below for details.
		"""

	@CLIArgument()
	class FlagMaxMemorySize(ShortTupleFlag, name="M"):
		"""
		Set the maximum amount of memory in bytes used for the internal representations of design units. The default is
		16 megabytes but this may be insufficient when elaborating a large design. The size parameter takes an optional k,
		m, or g suffix to indicate kilobytes, megabytes, and gigabytes respectively. For example -M64m for 64 megabytes.
		"""

	@CLIArgument()
	class FlagLibraryMapping(LongKeyValueFlag, name="map", pattern="--{0}={1}:{2}"):
		"""
		Specify exactly the location of the logical library name. Libraries mapped in this way will not use the normal
		search path.
		"""

	@CLIArgument()
	class FlagMessages(LongValuedFlag, name="messages"):
		"""
		Select the format used for printing error and informational messages. The default full message format is designed
		for readability whereas the compact messages can be easily parsed by tools.
		"""

	@CLIArgument()
	class FlagRandomSeed(LongValuedFlag, name="seed"):
		"""
		Seed for random number generation. Affects the ‘get_random’ function in the ‘nvc.random’ package, the ``--shuffle``
		option, and PSL union expressions.
		"""

	@CLIArgument()
	class FlagVHDLStandard(LongValuedFlag, name="std"):
		"""
		Select the VHDL standard revision to use. VHDL standard revisions are commonly referred to by the year they were
		published. For example IEEE 1076-1993 is known as VHDL-93. Specify either the full year such as 1993 or just the
		last two digits such as ``93``. The accepted revisions are 1993, 2000, 2002, 2008, 2019. Note there is very limited
		supported VHDL-2019 at present and VHDL-87 is not supported. The default standard revision is VHDL-2008.
		"""
		_value: VHDLVersion

		def __init__(self, value: VHDLVersion):
			if value is None:
				raise ValueError(f"")  # FIXME: add message

			self._value = value

		@property
		def Value(self) -> VHDLVersion:
			return self._value

		@Value.setter
		def Value(self, value: VHDLVersion) -> None:
			if value is None:
				raise ValueError(f"")  # FIXME: add message

			self._value = value

		def AsArgument(self) -> Union[str, Iterable[str]]:
			if self._name is None:
				raise ValueError(f"")  # FIXME: add message

			return self._pattern.format(self._name, str(self._value)[-2:])

	@CLIArgument()
	class FlagRandomSeed(LongValuedFlag, name="stderr"):
		"""
		Print error messages with the given severity or higher to ‘stderr’ instead of ‘stdout’. The default is to print all
		messages to ‘stderr’. Valid levels are note, warning, error, failure, and none.
		"""

	@CLIArgument()
	class FlagLibrary(LongValuedFlag, name="work"):
		"""
		Use name as the work library. The second variant explicitly specifies the location of the library.
		"""

	@CLIArgument()
	class CommandTCLScript(LongTupleFlag, name="do"):
		"""
		Evaluate a batch TCL script, optionally with *unit* loaded.
		"""

	@CLIArgument()
	class CommandAnalyze(ShortFlag, name="a"):
		"""Analyze VHDL source file(s)."""

	@CLIArgument()
	class OptionPaths(PathListArgument):
		"""Add list of VHDL files to analyze."""

	@CLIArgument()
	class FlagRelaxed(LongFlag, name="relaxed"):
		"""Relax some LRM rules."""

	@CLIArgument()
	class CommandElaborate(ShortTupleFlag, name="e"):
		"""Elaborate design."""

	@CLIArgument()
	class CommandRun(ShortTupleFlag, name="r"):
		"""Simulate design."""







	def _CopyParameters(self, tool: "NVC") -> None:
		for key in self.__cliParameters__:
			if self._NeedsParameterInitialization(key):
				value = self.__cliParameters__[key].Value
				tool.__cliParameters__[key] = key(value)
			else:
				tool.__cliParameters__[key] = key()

	def _SetParameters(self, tool: "NVC", std: Nullable[VHDLVersion] = None):
		if std is not None:
			tool[self.FlagVHDLStandard] = str(std)

	def GetNVCAsAnalyzer(self, std: Nullable[VHDLVersion] = None) -> "NVC":
		tool = NVC(executablePath=self._executablePath)

		tool[tool.CommandAnalyze] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std)

		return tool

	def GetNVCAsElaborator(self, std: Nullable[VHDLVersion] = None) -> "NVC":
		tool = NVC(executablePath=self._executablePath)

		tool[tool.CommandElaborate] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std)

		return tool

	def GetNVCAsSimulator(self, std: Nullable[VHDLVersion] = None) -> "NVC":
		tool = NVC(executablePath=self._executablePath)

		tool[tool.CommandRun] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std)

		return tool

	def Help(self) -> str:
		tool = NVC(executablePath=self._executablePath)

		tool[tool.CommandHelp] = True

		tool.StartProcess()
		return "\n".join(tool.GetLineReader())

	def Version(self) -> NVCVersion:
		tool = NVC(executablePath=self._executablePath)

		tool[tool.CommandVersion] = True

		tool.StartProcess()
		iterator = iter(tool.GetLineReader())
		firstLine = next(iterator)

		return NVCVersion(firstLine)
