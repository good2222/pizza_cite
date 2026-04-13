from django.conf import settings


def static_version(request):
    """Додає STATIC_VERSION у шаблони — змініть число в settings, щоб оновити CSS у браузері."""
    return {
        'STATIC_VERSION': getattr(settings, 'STATIC_VERSION', 1),
    }
