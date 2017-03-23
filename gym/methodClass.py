from django.db import connection


def select_all_room1(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM  WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row