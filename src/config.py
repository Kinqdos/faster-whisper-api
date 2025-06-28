import json
import os.path
import shutil

from pydantic import BaseModel
from pydantic import PositiveInt


class Config(BaseModel):
    model: str
    compute_type: str
    device: str
    max_processes: PositiveInt


def load_config(path_or_dir: str) -> Config:
    config_path = path_or_dir if path_or_dir.endswith(".json") else os.path.join(path_or_dir, "config.json")

    # Copy default config, if no config is present
    if not os.path.exists(config_path):
        print("No config file found, creating default config")
        shutil.copy2("./config.json", config_path)

    with open(config_path, 'r') as file:
        data = json.load(file)
        return Config(**data)
