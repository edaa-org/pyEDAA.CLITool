from pyTooling.CLIAbstraction            import CLIOption, Executable
from pyTooling.CLIAbstraction.Argument   import LongValuedFlagArgument


class GTKWave(Executable):
	_executableNames = {
		"Linux":   "gtkwave",
		"Windows": "gtkwave.exe"
	}

	@CLIOption
	class FlagDumpFile(LongValuedFlagArgument, name="dump"): ...

	@CLIOption
	class FlagSaveFile(LongValuedFlagArgument, name="save"): ...
