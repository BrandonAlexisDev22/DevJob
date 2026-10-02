# DevJob

Plataforma de empleo especializada para desarrolladores.

## Tecnologías

- Python
- Django
- Django REST Framework
- PostgreSQL
- Git
- GitHub

## Arquitectura de aplicaciones

El proyecto se divide en apps de Django, cada una responsable de un dominio del negocio. La configuración global vive en `config/`.

| App | Responsabilidad | Ruta base |
|-----|-----------------|-----------|
| `core` | Funcionalidad transversal compartida por el resto de apps: utilidades, modelos base abstractos y endpoints de sistema (p. ej. health check). No contiene lógica de negocio. | `/` |
| `users` | Gestión de usuarios: registro, autenticación, perfiles de desarrolladores y roles. | `/api/users/` |
| `companies` | Empresas que publican ofertas: perfil de empresa, datos de contacto y miembros reclutadores. | `/api/companies/` |
| `jobs` | Ofertas de empleo: creación, edición, publicación, búsqueda y filtrado (tecnologías, modalidad, salario, etc.). | `/api/jobs/` |
| `applications` | Postulaciones de desarrolladores a ofertas: envío, seguimiento y cambios de estado del proceso de selección. | `/api/applications/` |

### Dependencias entre dominios

- `core` no depende de ninguna otra app.
- `users` y `companies` pueden depender de `core`.
- `jobs` depende de `companies` (cada oferta pertenece a una empresa).
- `applications` depende de `users` y `jobs` (un usuario se postula a una oferta).

### Estructura de cada app

Todas las apps siguen la misma estructura:

```
<app>/
├── migrations/
├── __init__.py
├── admin.py      # Registro de modelos en el admin
├── apps.py       # Configuración de la app
├── models.py     # Modelos del dominio
├── tests.py      # Pruebas
├── urls.py       # Rutas de la app (incluidas en config/urls.py)
└── views.py      # Vistas / endpoints
```

## Instalación

### 1. Clonar el repositorio

### 2. Crear entorno virtual

### 3. Instalar dependencias

### 4. Configurar variables de entorno

### 5. Ejecutar migraciones

### 6. Ejecutar servidor