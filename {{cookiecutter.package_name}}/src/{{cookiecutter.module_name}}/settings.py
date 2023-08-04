import logging
import os
import yaml
from dataclasses import dataclass, field, asdict
from typing import List
from pathlib import Path


log_format = "%(levelname)s: [%(asctime)s] %(message)s [%(module)s:%(funcName)s]"
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(fmt=log_format))
log.addHandler(handler)

BOLD = "\033[1m"
END = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


@dataclass
class Settings:
    greet: str = field(default_factory=lambda: os.environ.get("GREET", "world"))
    many_times: int = field(default_factory=lambda: int(os.environ.get("MANY_TIMES", "2")))


def parse_settings(file_path: str) -> Settings:
    if os.path.exists(Path(file_path)):
        with open(file_path) as yaml_file:
            log.info(f"Loading settings from {BOLD}{file_path}{END}")
            yaml_data = yaml.safe_load(yaml_file)
            config_dict = asdict(Settings())
            for key, value in yaml_data.items():
                if key in config_dict:
                    config_dict[key] = value
                else:
                    log.info(f"Property {key} found in the YAML will not be used")
            return Settings(**config_dict)
    else:
        return Settings()

settings = parse_settings("settings.yml")


