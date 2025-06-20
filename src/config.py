import json

from pydantic import BaseModel
from pydantic import PositiveInt


class Config(BaseModel):
    model: str
    compute_type: str
    device: str = "auto"
    max_processes: PositiveInt

def load_config() -> Config:
    with open('./config.json', 'r') as file:
        data = json.load(file)
        return Config(**data)