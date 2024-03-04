import os

from src.packages.constants.environ_constants import EnvironConstants


class PathConstants:
    DEFAULT_PROJECT_PATH: str = ''
    DEFAULT_DB_PATH: str = ''
    CONF_NAME: str = 'config'

    def __init__(self):
        self.environ_constants = EnvironConstants()

        # Set root folder
        self.PROJECT_PATH = os.environ.get('PROJECT_PATH', PathConstants.DEFAULT_PROJECT_PATH)
        self.DATA_FOLDER = os.path.join(self.PROJECT_PATH, 'data')
        self.CDB_DATASET_PATH = os.path.join(self.DATA_FOLDER, 'cdb_90', 'data')
        self.MODELS_FOLDER = os.path.join(self.PROJECT_PATH, 'models')
