"""
Configuración de desarrollo local.

Uso: DJANGO_SETTINGS_MODULE=config.settings.dev (valor por defecto en manage.py)
"""

from .base import *  # noqa: F403
from .base import ALLOWED_HOSTS, env_bool

DEBUG = env_bool("DEBUG", True)

ALLOWED_HOSTS = ALLOWED_HOSTS or ["localhost", "127.0.0.1"]
