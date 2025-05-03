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
# Copyright 2014-2016 Technische Universitaet Dresden - Germany, Chair of VLSI-Design, Diagnostics and Architecture    #
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
"""An abstraction layer of EDA CLI tools."""
__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2014-2025, Patrick Lehmann, Unai Martinez-Corral"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.3.6"
__keywords__ =  ["cli", "abstraction layer", "eda"]

from pathlib import Path
from typing  import Any, Optional as Nullable

from pyTooling.Decorators  import export
from pyTooling.Exceptions  import ExceptionBase
from pyTooling.MetaClasses import ExtendedType


@export
class CLIToolException(ExceptionBase):
	"""Base-class for all pyEDAA.CLITool specific exceptions."""


class ToolMixIn(metaclass=ExtendedType, mixin=True):
	_platform: str
	_dryrun: bool
	_binaryDirectoryPath: Path
	_version: str
	_logger: Any

	def __init__(self, platform: str, dryrun: bool, binaryDirectoryPath: Path, version: str, logger: Nullable[Any] =None):
		self._platform =            platform
		self._dryrun =              dryrun
		self._binaryDirectoryPath = binaryDirectoryPath
		self._version =             version
		self._logger =              logger
		# self._environment =         Environment()
