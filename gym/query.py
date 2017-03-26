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

def my_sql_query_1(self):
    with connection.cursor() as cursor:
        # 1. SELECTION QUERY = Select a specific equipment with a specified type and display all tuples
        cursor.execute("SELECT * FROM equipment WHERE EquipType = equipment")

def my_sql_query_2(self):
    with connection.cursor() as cursor:
        # 1. SELECTION QUERY = Select a specific room with a specified type and display all tuples
        cursor.execute("SELECT * FROM room1 WHERE roomType = type")

def my_sql_query_3(self):
    with connection.cursor() as cursor:
        # 1. PROJECTION QUERY = View the custIDs of all customers that currently booked a room
        cursor.execute("SELECT customerID FROM reservedRoom, room, customer WHERE customerID = reservedRoom.customerID and room.roomID = reservedRoom.customerID")

def my_sql_query_4(self):
    with connection.cursor() as cursor:
        # 1. PROJECTION QUERY = View the custIDs of all customers that currently booked equipment
        # EDIT THIS QUERY BUT TOO TIRED NOW
        cursor.execute("SELECT customerID FROM Equipment, customer WHERE customerID = Equipment.customerID")

def my_sql_query_5(self):
    with connection.cursor() as cursor:
        # 2. JOIN = Get custID’s of customers who booked rooms
        cursor.execute("SELECT custID FROM ((reservedRoom INNER JOIN customer1 ON reservedRoom.customerID = customer1.customerID) INNER JOIN room1 ON reservedRoom.customerID = room1.roomID")

def my_sql_query_6(self):
    with connection.cursor() as cursor:
        # 2. JOIN = Get custID’s of customers who booked equipment
        cursor.execute("SELECT custID FROM Equipment_checkIn_reserveOrcancel_return2 INNER JOIN customer1 ON Equipment_checkIn_reserveOrcancel_return2.EquipCustID = customer1.customerID")

def my_sql_query_7(self):
    with connection.cursor() as cursor:
        # 3. DIVISION = Get all athletes who reserved every unique equipment (with a certain type) during this week
        cursor.execute("SELECT ...")

def my_sql_query_8(self):
    with connection.cursor() as cursor:
        # 4. AGGREGATION = Total # of rooms booked during the week for all customers
        cursor.execute("SELECT Count(*) FROM reservedRoom")

def my_sql_query_9(self):
    with connection.cursor() as cursor:
        # 4. AGGREGATION = Total # of equipment booked during the week for all customers
        cursor.execute("SELECT Count(*) FROM Equipment_checkIn_reserveOrcancel_return2")

def my_sql_query_10(self):
    with connection.cursor() as cursor:
        # 5. NESTED AGGREGATION = Type of Equipment with the MOST currently in stock
        cursor.execute(
            "SELECT e.equipType FROM Equipment_checkIn_reserveOrcancel_return1 e  WHERE e.equipRate = (SELECT MAX(e1.equipRate) From Equipment_checkIn_reserveOrcancel_return1  e1) GROUP BY e.equipType")

def my_sql_query_11(self):
    with connection.cursor() as cursor:
        # 5. NESTED AGGREGATION = Type of Equipment with the LEAST currently in stock
        cursor.execute(
            "SELECT e.equipType FROM Equipment_checkIn_reserveOrcancel_return1 e  WHERE e.equipRate = (SELECT MIN(e1.equipRate) From Equipment_checkIn_reserveOrcancel_return1  e1) GROUP BY e.equipType")

def my_sql_query_12(self):
    with connection.cursor() as cursor:
        # 6. DELETE WITHOUT CASCADE = Delete a tuple in clean with a given RoomID, time, and employee ID
        cursor.execute(
            "DELETE FROM clean WHERE employeeID = employee ID and employeeroomID = roomID and employeeTIME = time")

def my_sql_query_13(self):
    with connection.cursor() as cursor:
        # 6. DELETE WITH CASCADE = Delete an item from items (and delete any trace of it with a given ItemID)
        cursor.execute("DELETE ...")

def my_sql_query_14(self):
    with connection.cursor() as cursor:
        # 7. UPDATE = roomRate
        cursor.execute("Update room2 Set roomRate = inputedPrice Where ItemID = ID")

def my_sql_query_15(self):
    with connection.cursor() as cursor:
        # 7. UPDATE = equipmentRate
        cursor.execute("Update Equipment_checkIn_reserveOrcancel_return1 Set equipmentRate = inputedPrice Where ItemID = ID")
