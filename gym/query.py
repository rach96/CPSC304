import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE room1 SET roomID = 111 WHERE room1 = room1", [self.room1])
        cursor.execute("SELECT roomID FROM room1 WHERE roomID = 111", [self.room1])
        row = cursor.fetchone()

    return row