"""
WSGI config for CPSC304Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import os, sys

sys.path.append('/Desktop/cpsc304/304 project/CPSC304/CPSC304')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CPSC304Project.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
