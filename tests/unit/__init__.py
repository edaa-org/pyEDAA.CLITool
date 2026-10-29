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
# Copyright 2021-2026 Electronic Design Automation Abstraction (EDA²)                                                  #
# Copyright 2017-2020 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""
Helper classes for unit tests.
"""
from pathlib  import Path
from platform import system
from shutil   import which
from typing   import Optional as Nullable


class Helper:
	_system = system()

	@classmethod
	def getExecutablePath(cls, programName: str, binaryDirectory: Nullable[Path] = None) -> str:
		"""
		Return the executable's path as a program's :func:`repr` writes it.

		Without a binary directory, a program found in ``PATH`` is written with its full path. Backslashes are escaped.

		:param programName:     The program's name without extension.
		:param binaryDirectory: Optional, the directory containing the program.
		:returns:               The path as written inside the string literal of :func:`repr`.
		"""
		extensions = ".exe" if cls._system == "Windows" else ""
		programName = f"{programName}{extensions}"
		if binaryDirectory is not None:
			path = str(binaryDirectory / programName)
		else:
			path = which(programName) or programName

		return path.replace("\\", "\\\\")
