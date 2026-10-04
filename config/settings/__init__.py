"""
Per-environment Django settings.

Available modules:
- config.settings.dev      (local development, default in manage.py)
- config.settings.staging
- config.settings.prod     (default in wsgi.py and asgi.py)

Secrets and per-environment values are read from environment variables or
from a .env file at the project root (see .env.example).
"""
