import sys
from .base import *

DEBUG = True

DATABASES['default'] = DATABASES['development']

# Django development dependencies
INSTALLED_APPS.append('django_extensions')



