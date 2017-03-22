import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from django.db import connection
import argparse
from django.db import connection, transaction

def my_custom_sql(self):
    with connection.cursor() as cursor:

        #parser = argparse.ArgumentParser(description='Executes a raw database script on a Django project.')
        #parser.add_argument('filenames', action='append', metavar='FILE', type=str,
        #                    help='A file name or list of file names of database '
        #                         'scripts to be executed.')
        #args = parser.parse_args()

        cursor = connection.cursor()
       # for filename in args.filenames:
        f = open('gym/tables.sql')

        response = cursor.executescript(f.read())
        f.close()
        rows = cursor.fetchall()
        for row in rows:
            print
            repr(row)

        return rows