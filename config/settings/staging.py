"""
Staging settings. Inherits from production and only overrides what is needed.

Usage: DJANGO_SETTINGS_MODULE=config.settings.staging
"""

from .prod import *  # noqa: F403
