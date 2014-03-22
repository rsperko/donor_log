"""
WSGI config for donor_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "donor_log.settings")

from django.core.wsgi import get_wsgi_application
from django.conf import settings


if settings.IN_PROD == True:
    from dj_static import Cling
    application = Cling(get_wsgi_application())
else:
    application = get_wsgi_application()
