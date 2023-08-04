"""{{ cookiecutter.short_description.rstrip(".") }}."""

__version__ = "0.0.1"

from .settings import Settings, parse_settings
from .api import Api
