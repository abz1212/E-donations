"""ASGI config for E-donations project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_donations.settings")

application = get_asgi_application()
