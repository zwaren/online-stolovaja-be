import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_stolovaja_be.settings')

import django

django.setup()
from django.contrib.auth.models import Group


GROUPS = ['user', 'staff', 'cook', 'admin']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)