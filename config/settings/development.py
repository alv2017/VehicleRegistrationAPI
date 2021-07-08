import sys
from .base import *

DEBUG = True

DATABASES['default'] = DATABASES['development']
print(DATABASES['default'])

if 'test' in sys.argv or 'pytest' in sys.argv:
    DATABASES['default'] = DATABASES['test']

INSTALLED_APPS.append('django_extensions')



