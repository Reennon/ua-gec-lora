import logging

import dynaconf
from singleton_decorator import singleton

from src.packages.constants.config_constants import ConfigConstants


@singleton
class ParameterServer:
    def __init__(self):
        logging.debug('Initialized ParameterServer')

        settings = dynaconf.Dynaconf(
            settings_files=ConfigConstants.CONFIG_FILES
        )
        self.settings = settings

        logging.debug('Loaded config parameters into ParameterServer')
