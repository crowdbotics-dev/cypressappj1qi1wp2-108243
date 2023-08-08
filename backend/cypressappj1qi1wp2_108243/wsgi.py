"""
WSGI config for cypressappj1qi1wp2_108243 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cypressappj1qi1wp2_108243.settings')

application = get_wsgi_application()
