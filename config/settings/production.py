import os

from .base import *

SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-24#+mypq*=1v77s(37v+_$t!p7+iwdnq)$q&djz85vo$9f5sym"
)
ALLOWED_HOSTS = [host for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host]

DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "t", "yes")
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [f"https://{site}" for site in ALLOWED_HOSTS]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False  # Handled by nginx

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "wagtail_db",
        "USER": "wagtail",
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "1234"),
        "HOST": "wagtail_db",
        "PORT": 5432,
    }
}

try:
    from .local import *
except ImportError:
    pass
