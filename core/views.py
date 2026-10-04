"""Views for the core app (project-wide endpoints)."""

from django.http import JsonResponse


def health_check(request):
    """Return a simple JSON payload to confirm the service is up."""
    return JsonResponse({"status": "ok"})
