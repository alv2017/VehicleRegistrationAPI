import sys
from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES['default'] = DATABASES['production']

if 'test' in sys.argv or 'pytest' in sys.argv:
    DATABASES['default'] = DATABASES['test']

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True