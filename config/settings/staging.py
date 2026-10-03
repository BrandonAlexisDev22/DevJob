"""
Configuración de staging. Hereda de producción y solo cambia lo necesario.

Uso: DJANGO_SETTINGS_MODULE=config.settings.staging
"""

from .prod import *  # noqa: F403
