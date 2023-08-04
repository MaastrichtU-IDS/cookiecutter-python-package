"""Example class."""
from typing import Optional

from {{cookiecutter.module_name}}.settings import Settings, log


class Api:
    def __init__(self, settings: Optional[Settings] = None) -> None:
        self.settings = settings if settings else Settings()
        log.info(self.settings)

    def hello_world(self, label: Optional[str] = None) -> str:
        label = label if label else self.settings.greet
        out = ""
        for i in range(self.settings.many_times):
            out += f"[{i}] Hello {label} "
        return out
