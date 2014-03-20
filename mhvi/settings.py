"""
Django settings for mhvi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import socket

# TODO set up heroku environment variable
if socket.gethostname() == 'poseiden.local':
    from settings_dev import *
else:
    from settings_prod import *
