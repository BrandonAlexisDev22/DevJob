"""
Configuración de Django por entorno.

Módulos disponibles:
- config.settings.dev      (desarrollo local, usado por defecto en manage.py)
- config.settings.staging
- config.settings.prod     (usado por defecto en wsgi.py y asgi.py)

Los secretos y valores por entorno se leen desde variables de entorno o desde
un archivo .env en la raíz del proyecto (ver .env.example).
"""
