"""
WSGI config for qblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/pi-hackathon')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pi-hackathon.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
