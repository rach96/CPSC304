#!/usr/bin/env python
# Load the Django environment
import os

import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fooproject.settings")
from django.conf import settings

try:
    project_path = os.environ['DJANGO_PROJECT_PATH']
except KeyError:
    raise Exception("Unable to locate Django project.  Set your operating "
                    "system's DJANGO_PROJECT_PATH environment variable to "
                    "point to the root of the Django project.")

if project_path not in sys.path:
    sys.path.append(project_path)

settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
if settings_module:
    settings = __import__(settings_module)
else:
    import settings
os.environ.setdefault(settings)
# End Django environment load.
import argparse
from django.db import connection, transaction

parser = argparse.ArgumentParser(description='Executes a raw database script on a Django project.')
parser.add_argument('filenames', action='append', metavar='FILE', type=str,
                    help='A file name or list of file names of database '
                         'scripts to be executed.')
args = parser.parse_args()

cursor = connection.cursor()
for filename in args.filenames:
    f = open("./sql_tables.py")
    response = cursor.execute(f.read())
    f.close()
    rows = cursor.fetchall()

