from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

MAIN_DATABASE_URL = config("MAIN_DATABASE_URL", cast=Secret)

TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)