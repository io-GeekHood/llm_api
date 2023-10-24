from copy import deepcopy
from llm_api.config.config import Config
import yaml


def read(config: Config) -> Config:
    config = deepcopy(config)
    with open(config.config_file) as f:
        config.update(**yaml.safe_load(f))
    return config
