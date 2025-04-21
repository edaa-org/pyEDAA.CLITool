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
# Copyright 2017-2025 Patrick Lehmann - Boetzingen, Germany                                                            #
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
from re                    import search as re_search
from typing                import Union, Iterable, Tuple, Optional as Nullable

from pyTooling.Decorators  import export
from pyTooling.MetaClasses import ExtendedType
from pyVHDLModel           import VHDLVersion

from pyTooling.CLIAbstraction               import CLIArgument, Executable
from pyTooling.CLIAbstraction.Argument      import PathListArgument, StringArgument
from pyTooling.CLIAbstraction.Command       import CommandArgument
from pyTooling.CLIAbstraction.Flag          import ShortFlag, LongFlag
from pyTooling.CLIAbstraction.BooleanFlag   import LongBooleanFlag
from pyTooling.CLIAbstraction.ValuedFlag    import ShortValuedFlag, LongValuedFlag
from pyTooling.CLIAbstraction.KeyValueFlag  import ShortKeyValueFlag

from pyEDAA.CLITool       import CLIToolException


@export
class GHDLVersion(metaclass=ExtendedType, slots=True):
	_major: int
	_minor: int
	_micro: int
	_dev: bool
	_commitsSinceLastTag: int
	_gitHash: str
	_dirty: bool
	_edition: str
	_gnatCompiler: Tuple[int, int, int]
	_backend: str

	VERSION_LINE_PATTERN = (
		r"GHDL"
		r"\s(?P<Major>\d+)\.(?P<Minor>\d+)\.(?P<Micro>\d+)(?:-(?P<Suffix>dev|rc\d+))?"
		r"\s\((?:"
			r"(?:"
				r"(?P<Packaging>tarball)"
			r")|(?:"
				r"[a-z]?(?P<major2>\d+)\.(?P<minor2>\d+)\.(?P<micro2>\d+)\.(?:r(?P<cslt>\d+))\.(?:g(?P<Hash>[0-9a-f]+))(?:\.(?P<Dirty>dirty))?"
			r")|(?:"
				r"Ubuntu\s(?P<UbuntuMajor>\d+)\.(?P<UbuntuMinor>\d+)\.(?P<UbuntuMicro>\d+)\+dfsg-(?P<dfsg>\d+)ubuntu(?P<UbuntuPackage>\d+)"
			r")"
		r")\)"
		r"\s\[(?P<Edition>[\w\s]+)\]"
	)
	GNAT_LINE_PATTERN = (
		r"\s*[\w\s]+:\s"
		r"(?:"
			r"(?:(?P<Major>\d+)\.(?P<Minor>\d+)\.(?P<Micro>\d+))"
		r"|"
			r"(?:Community\s(?P<Year>\d{4})\s\((?P<DateCode>\d{8}-\d{2})\))"
		r")"
	)
	BACKEND_LINE_PATTERN = (
		r"\s*"
		r"(?:static elaboration, )?"
		r"(?P<Backend>llvm|mcode|gcc)"
		r"(?: (?P<LLVMMajor>\d+)\.(?P<LLVMMinor>\d+)\.(?P<LLVMMicro>\d+))?"
		r"(?: JIT)?"
		r" code generator"
	)

	def __init__(self, versionLine: str, gnatLine: str, backendLine: str):
		match = re_search("^" + self.VERSION_LINE_PATTERN + "$", versionLine)
		if match is None:
			raise CLIToolException(f"Unknown first GHDL version string '{versionLine}'.")

		self._major = int(match["Major"])
		self._minor = int(match["Minor"])
		self._micro = int(match["Micro"])
		if (suffix := match["Suffix"]) is not None:
			self._dev = suffix == "dev"
		else:
			self._dev = False
		if (cslt := match["cslt"]) is not None:
			self._commitsSinceLastTag = int(cslt)
		else:
			self._commitsSinceLastTag = 0
		self._gitHash = match["Hash"]
		self._dirty = "Dirty" in match.groups()
		self._edition = match["Edition"]

		match = re_search("^" + self.GNAT_LINE_PATTERN + "$", gnatLine)
		if match is None:
			raise CLIToolException(f"Unknown second GHDL version string '{gnatLine}'.")

		if match["Year"] is None:
			self._gnatCompiler = (int(match["Major"]), int(match["Minor"]), int(match["Micro"]))
		else:
			self._gnatCompiler = (int(match["Year"]), 0, 0)

		match = re_search("^" + self.BACKEND_LINE_PATTERN + "$", backendLine)
		if match is None:
			raise CLIToolException(f"Unknown third GHDL version string '{backendLine}'.")

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
	def Dev(self) -> bool:
		return self._dev

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
	def Edition(self) -> str:
		return self._edition

	def __str__(self) -> str:
		dev = f"-dev" if self._dev else ""
		return f"{self._major}.{self._minor}.{self._micro}{dev}"

	def __repr__(self) -> str:
		return f"{self.__str__()} (Backend: {self._backend}; Git: {self._gitHash})"


@export
class GHDL(Executable):
	_executableNames = {
		"Darwin":  "ghdl",
		"FreeBSD": "ghdl",
		"Linux":   "ghdl",
		"Windows": "ghdl.exe"
	}

	# XXX: overwrite __init__ and get backend variant
	# XXX: check for compatible backends

	@CLIArgument()
	class CommandHelp(CommandArgument, name="help"):
		"""Print help page(s)."""

	@CLIArgument()
	class CommandVersion(CommandArgument, name="version"):
		"""Print version information."""

	@CLIArgument()
	class CommandSyntax(CommandArgument, name="syntax"):
		"""Check syntax."""

	@CLIArgument()
	class CommandElaborationOrder(CommandArgument, name="elab-order"):
		"""Display (elaboration) ordered source files."""

	@CLIArgument()
	class CommandAnalyze(CommandArgument, name="analyze"):
		"""Analyze VHDL source file(s)."""

	@CLIArgument()
	class CommandElaborate(CommandArgument, name="elaborate"):
		"""Elaborate design."""

	@CLIArgument()
	class CommandElaborationAndRun(CommandArgument, name="elab-run"):
		"""Elaborate and simulate design."""

	@CLIArgument()
	class CommandRun(CommandArgument, name="run"):
		"""Simulate design."""

	@CLIArgument()
	class CommandBind(CommandArgument, name="bind"):
		"""Bind design unit."""

	@CLIArgument()
	class CommandLink(CommandArgument, name="link"):
		"""Link design unit."""

	@CLIArgument()
	class CommandListLink(CommandArgument, name="list-link"):
		"""List objects file to link a design unit."""

	@CLIArgument()
	class CommandCompile(CommandArgument, name="compile"):
		"""Generate whole sequence to elaborate design from files."""

	@CLIArgument()
	class CommandGenerateDependencies(CommandArgument, name="gen-depends"):
		"""Generate dependencies of design."""

	@CLIArgument()
	class CommandSynthesize(CommandArgument, name="synth"):
		"""Synthesis from design unit."""

	@CLIArgument()
	class FlagVerbose(ShortFlag, name="v"):
		"""Run in verbose mode (print more messages)."""

	# Analyze and elaborate options
	@CLIArgument()
	class FlagVHDLStandard(LongValuedFlag, name="std"):
		"""Set the used VHDL standard version."""
		_value: VHDLVersion

		def __init__(self, value: VHDLVersion):
			if value is None:
				raise ValueError(f"")  # XXX: add message

			self._value = value

		@property
		def Value(self) -> VHDLVersion:
			return self._value

		@Value.setter
		def Value(self, value: VHDLVersion) -> None:
			if value is None:
				raise ValueError(f"")  # XXX: add message

			self._value = value

		def AsArgument(self) -> Union[str, Iterable[str]]:
			if self._name is None:
				raise ValueError(f"")  # XXX: add message

			return self._pattern.format(self._name, str(self._value)[-2:])

	@CLIArgument()
	class FlagIEEEFlavor(LongValuedFlag, name="ieee"):
		"""Set the used VHDL flavor."""

	@CLIArgument()
	class FlagSynopsys(ShortFlag, name="fsynopsys"):
		"""Set used VHDL flavor to *Synopsys* and make Synopsys packages visible in library ``ìeee``."""

	@CLIArgument()
	class FlagRelaxed(ShortFlag, name="frelaxed"):
		"""Relax some LRM rules."""

	@CLIArgument()
	class FlagExplicit(ShortFlag, name="fexplicit"): ...

	@CLIArgument()
	class FlagLibrary(LongValuedFlag, name="work"):
		"""Set working library."""

	@CLIArgument()
	class FlagWorkingDirectory(LongValuedFlag, name="workdir"):
		"""Set working directory."""

	@CLIArgument()
	class FlagMultiByteComments(LongFlag, name="mb-comments"):
		"""Allow multi-byte comments."""

	@CLIArgument()
	class FlagSyntesisBindingRule(LongFlag, name="syn-binding"):
		"""Enable synthesis binding rule."""

	@CLIArgument()
	class FlagSearchPath(ShortValuedFlag, name="P", pattern="-{0}{1}"):
		"""Add search path."""

	@CLIArgument()
	class FlagTimeResolution(LongValuedFlag, name="time-resolution"):
		"""Set base time resolution.

		Allowed values are ``auto`` (default), ``fs``, ``ps``, ``ns``, ``us``, ``ms`` or ``sec``.
		"""

	@CLIArgument()
	class FlagVitalChecks(LongBooleanFlag, name="vital-checks", pattern="-{0}", falsePattern="--no-{0}"):
		"""Check VITAL restrictions."""

	@CLIArgument()
	class FlagWarnUnboundComponents(ShortFlag, name="binding", pattern="-W{0}"):
		"""Warns for unbound components."""

	@CLIArgument()
	class FlagWarnReservedWords(ShortFlag, name="reserved", pattern="-W{0}"):
		"""Warns if VHDL'93 reserved words are used in VHDL'87."""

	@CLIArgument()
	class FlagWarnRedefinedDesignUnits(ShortFlag, name="library", pattern="-W{0}"):
		"""Warns for redefined design unit."""

	@CLIArgument()
	class FlagWarnNonVitalGenericNames(ShortFlag, name="vital-generic", pattern="-W{0}"):
		"""Warns of non-vital generic names."""

	@CLIArgument()
	class FlagWarnElaborationChecks(ShortFlag, name="delayed-checks", pattern="-W{0}"):
		"""Warns for checks performed at elaboration."""

	@CLIArgument()
	class FlagWarnUnnecessaryPackageBody(ShortFlag, name="body", pattern="-W{0}"):
		"""Warns for unnecessary package body."""

	@CLIArgument()
	class FlagWarnOthersSpecifications(ShortFlag, name="specs", pattern="-W{0}"):
		"""Warns if an all/others specification does not apply."""

	@CLIArgument()
	class FlagUnused(ShortFlag, name="unused", pattern="-W{0}"):
		"""Warns for unused subprograms."""

	@CLIArgument()
	class FlagError(ShortFlag, name="error", pattern="-W{0}"):
		"""Turns warnings into errors."""

	@CLIArgument()
	class OptionPaths(PathListArgument):
		"""Add list of VHDL files to analyze."""

	@CLIArgument()
	class OptionTopLevel(StringArgument):
		"""Specify the toplevel design unit."""

	@CLIArgument()
	class OptionArchitecture(StringArgument):
		"""Specify the architecture name, if the toplevel design unit is an entity."""

	@CLIArgument()
	class FlagGenerics(ShortKeyValueFlag, pattern="-{0}{1}={2}"):
		"""Set a generic value."""

	@CLIArgument()
	class FlagAsserts(ShortValuedFlag, name="asserts"):
		"""Select how assertions are handled.

		It can be ``enable`` (the default), ``disable`` which disables all assertions and ``disable-at-0`` which disables
		only at the start of simulation.
		"""

	@CLIArgument()
	class FlagIEEEAsserts(ShortValuedFlag, name="ieee-asserts"):
		"""Select how assertions are handled.

		It can be ``enable`` (the default), ``disable`` which disables all assertions and ``disable-at-0`` which disables
		only at the start of simulation.
		"""

	@CLIArgument()
	class FlagStopTime(ShortValuedFlag, name="stop-time"):
		"""Stop the simulation after a given simulation time.

		The time is expressed as a time value, without any spaces. The time is the simulation time, not the real execution time.
		"""

	@CLIArgument()
	class FlagMaxDeltaCycles(ShortValuedFlag, name="stop-delta"):
		"""Stop the simulation after N delta cycles in the same current time."""

	@CLIArgument()
	class FlagDisplayDeltaCycles(ShortValuedFlag, name="disp-time"):
		"""Display the time and delta cycle number as simulation advances."""

	@CLIArgument()
	class FlagUnbufferedIO(ShortValuedFlag, name="unbuffered"):
		"""Disable buffering on STDOUT, STDERR and files opened in write or append mode (TEXTIO)."""

	@CLIArgument()
	class FlagReadWaveformOptionsFile(ShortValuedFlag, name="read-wave-opt"):
		"""Filter signals to be dumped to the waveform file according to the wavefile option file provided."""

	@CLIArgument()
	class FlagWriteWaveformOptionsFile(ShortValuedFlag, name="write-wave-opt"):
		"""If the wavefile option file doesn’t exist, creates it with all the signals of the design.
		Otherwise, it throws an error, because it won’t erase an existing file.
		"""

	@CLIArgument()
	class FlagGHWWaveformFile(ShortValuedFlag, name="wave"):
		"""Write the waveforms into a GHDL Waveform (``*.ghw``) file.

		Contrary to VCD files, any VHDL type can be dumped into a GHW file.
		"""

	def _CopyParameters(self, tool: "GHDL") -> None:
		for key in self.__cliParameters__:
			if self._NeedsParameterInitialization(key):
				value = self.__cliParameters__[key].Value
				tool.__cliParameters__[key] = key(value)
			else:
				tool.__cliParameters__[key] = key()

	def _SetParameters(self, tool: "GHDL", std: Nullable[VHDLVersion] = None, ieee: Nullable[str] = None):
		if std is not None:
			tool[self.FlagVHDLStandard] = str(std)

		if ieee is not None:
			tool[self.FlagVHDLStandard] = ieee

	def GetGHDLAsAnalyzer(self, std: Nullable[VHDLVersion] = None, ieee: Nullable[str] = None) -> "GHDL":
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandAnalyze] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std, ieee)

		return tool

	def GetGHDLAsElaborator(self, std: Nullable[VHDLVersion] = None, ieee: Nullable[str] = None) -> "GHDL":
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandElaborate] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std, ieee)

		return tool

	def GetGHDLAsSimulator(self, std: Nullable[VHDLVersion] = None, ieee: Nullable[str] = None) -> "GHDL":
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandRun] = True
		self._CopyParameters(tool)
		self._SetParameters(tool, std, ieee)

		return tool

	def Help(self) -> str:
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandHelp] = True

		tool.StartProcess()
		return "\n".join(tool.GetLineReader())

	def Version(self) -> GHDLVersion:
		tool = GHDL(executablePath=self._executablePath)

		tool[tool.CommandVersion] = True

		tool.StartProcess()
		iterator = iter(tool.GetLineReader())
		firstLine = next(iterator)
		secondLine = next(iterator)
		thirdLine = next(iterator)

		return GHDLVersion(firstLine, secondLine, thirdLine)
