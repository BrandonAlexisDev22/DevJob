"""
Configuración de producción.

Uso: DJANGO_SETTINGS_MODULE=config.settings.prod (valor por defecto en wsgi.py y asgi.py)

DEBUG siempre está apagado aquí, sin importar el valor de la variable DEBUG.
"""

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403
from .base import ALLOWED_HOSTS

DEBUG = False

if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("ALLOWED_HOSTS debe estar definido en producción.")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
