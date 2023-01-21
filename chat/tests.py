import os
import django
from django.test import TestCase

from faker import Faker

fake_gen = Faker('ru_RU')

try:
    os.environ['DJANGO_SETTINGS_MODULE'] = "config.settings"
except ModuleNotFoundError:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    os.environ['DJANGO_SETTINGS_MODULE'] = \
        f"{CURRENT_DIR.split('/')[-1]}.settings"
django.setup()




