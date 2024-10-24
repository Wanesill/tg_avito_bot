from functools import lru_cache
from os import getenv
from typing import Type, TypeVar

from pydantic import BaseModel, PostgresDsn, SecretStr
from yaml import load

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

ConfigType = TypeVar("ConfigType", bound=BaseModel)


class BotConfig(BaseModel):
    token: SecretStr


class DbConfig(BaseModel):
    dsn: PostgresDsn


@lru_cache(maxsize=1)
def __parse_config_file() -> dict:
    file_path = getenv("BOT_CONFIG")

    if file_path is None:
        error = "Could not find settings file"
        raise ValueError(error)

    with open(file_path, "rb") as file:
        config_data = load(file, Loader=SafeLoader)

    return config_data


@lru_cache
def get_config(model: Type[ConfigType], root_key: str) -> ConfigType:
    config_dict: dict = __parse_config_file()

    if root_key not in config_dict:
        error = f"Key {root_key} not found"
        raise ValueError(error)

    return model.model_validate(config_dict[root_key])
