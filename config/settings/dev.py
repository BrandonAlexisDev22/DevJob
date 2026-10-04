"""
Local development settings.

Usage: DJANGO_SETTINGS_MODULE=config.settings.dev (default in manage.py)
"""

from .base import *  # noqa: F403
from .base import ALLOWED_HOSTS, env_bool

DEBUG = env_bool("DEBUG", True)

ALLOWED_HOSTS = ALLOWED_HOSTS or ["localhost", "127.0.0.1"]
