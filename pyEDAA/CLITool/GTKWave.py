from pyTooling.CLIAbstraction            import CLIArgument, Executable
from pyTooling.CLIAbstraction.ValuedFlag import LongValuedFlag


class GTKWave(Executable):
	_executableNames = {
		"Linux":   "gtkwave",
		"Windows": "gtkwave.exe"
	}

	@CLIArgument()
	class FlagDumpFile(LongValuedFlag, name="dump"): ...

	@CLIArgument()
	class FlagSaveFile(LongValuedFlag, name="save"): ...
