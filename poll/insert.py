# insert_data_script.py
import os
import django

# Set the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poll.settings")
django.setup()

from vote.models import DemoTable

# Insert data
DemoTable.objects.create(name='John', age=25)
DemoTable.objects.create(name='Jane', age=30)
