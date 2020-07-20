"""WSGI config for E-donations project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_donations.settings")

application = get_wsgi_application()
