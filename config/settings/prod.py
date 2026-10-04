"""
Production settings.

Usage: DJANGO_SETTINGS_MODULE=config.settings.prod (default in wsgi.py and asgi.py)

DEBUG is always off here, regardless of the DEBUG environment variable.
"""

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403
from .base import ALLOWED_HOSTS

DEBUG = False

if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("ALLOWED_HOSTS must be set in production.")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
