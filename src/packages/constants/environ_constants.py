import os
from pydantic import parse_obj_as


class EnvironConstants:
    """
    Class wrapper for environment constants
    """

    PROJECT_PATH: str = parse_obj_as(str, os.environ.get('PROJECT_PATH', None))
    REDIS_HOST: str = parse_obj_as(str, os.environ.get('REDIS_HOST', None))
    REDIS_PORT: str = parse_obj_as(str, os.environ.get('REDIS_PORT', None))
    REDIS_URL: str = f'redis://{REDIS_HOST}:{REDIS_PORT}'
