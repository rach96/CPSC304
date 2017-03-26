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
        # 1. SELECTION QUERY = Select all the equipment with a specified type and display all tuples
        # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
        # NOTE = replace BASKETBALL with whatever the user inputs
        cursor.execute("SELECT * FROM Equipment_checkIn_reserveOrcancel_return1 WHERE EquipType ='Basketball' ")

def my_sql_query_2(self):
    with connection.cursor() as cursor:
        # 1. SELECTION QUERY = Select all the rooms with a specified type and display all tuples
        # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
        # NOTE = replace 'Large Gym Room' with whatever the user input
        cursor.execute("SELECT * FROM room1 WHERE roomType = 'Large Gym Room'")

def my_sql_query_3(self):
    with connection.cursor() as cursor:
        # 1. PROJECTION QUERY = View the custIDs and cusNames of all customers that currently booked a room
        # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
        # NOTE = currently nothing is displaying, but that may be due to the data that is currently stored
        cursor.execute("SELECT cusID, cusName FROM reservedRoom, room1, customer1 WHERE customerID = reservedRoom.customerID and room1.roomID = reservedRoom.customerID")

def my_sql_query_4(self):
    with connection.cursor() as cursor:
        # 1. PROJECTION QUERY = View the custIDs and cusNames of all customers that currently booked equipment
        # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
        # EDIT THIS QUERY BUT TOO TIRED NOW
        cursor.execute("SELECT cusID, cusName FROM Equipment_checkIn_reserveOrcancel_return2, customer1 WHERE cusID = Equipment_checkIn_reserveOrcancel_return2.EquipCustID")

def my_sql_query_5(self):
    with connection.cursor() as cursor:
        # 2. JOIN = Get custID’s of customers who booked rooms
        # Provide an interface for the user to choose this query
        cursor.execute("SELECT cusID FROM reservedRoom INNER JOIN customer1 ON reservedRoom.customerID = customer1.cusID INNER JOIN room1 ON reservedRoom.customerID = room1.roomID")

def my_sql_query_6(self):
    with connection.cursor() as cursor:
        # 2. JOIN = Get custID’s and cusName's of customers who booked equipment
        # Provide an interface for the user to choose this query
        cursor.execute("SELECT cusID, cusName FROM Equipment_checkIn_reserveOrcancel_return2 INNER JOIN customer1 ON Equipment_checkIn_reserveOrcancel_return2.EquipCustID = customer1.cusID")

def my_sql_query_7(self):
    with connection.cursor() as cursor:
        # 3. DIVISION = Get all athletes who reserved every unique equipment (with a certain type) during this week
        # Provide an interface for the user to choose this query
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
        # 5. NESTED AGGREGATION = Type of Equipment with the MOST cost
        cursor.execute(
            "SELECT e.equipType FROM Equipment_checkIn_reserveOrcancel_return1 e  WHERE e.equipRate = (SELECT MAX(e1.equipRate) From Equipment_checkIn_reserveOrcancel_return1  e1) GROUP BY e.equipType")

def my_sql_query_11(self):
    with connection.cursor() as cursor:
        # 5. NESTED AGGREGATION = Type of Equipment with the LEAST cost
        cursor.execute(
            "SELECT e.equipType FROM Equipment_checkIn_reserveOrcancel_return1 e WHERE e.equipRate = (SELECT MIN(e1.equipRate) From Equipment_checkIn_reserveOrcancel_return1  e1) GROUP BY e.equipType")

def my_sql_query_12(self):
    with connection.cursor() as cursor:
        # 6. DELETE WITHOUT CASCADE = Delete a tuple in clean with a given RoomID, time, and employee ID
        # Some input values would fail the cascade specification but others would successfully follow the cascade specification
        # NOTE = replace employeeID, employeeroomID, and employeeTIME with user input
        cursor.execute(
            "DELETE FROM clean WHERE employeeID = '1234' and employeeroomID = '0234' and employeeTime = 'Monday'")

def my_sql_query_13(self):
    with connection.cursor() as cursor:
        # 6. DELETE WITH CASCADE = Delete an item from items (and delete any trace of it with a given ItemID)
        cursor.execute("DELETE ...")

def my_sql_query_14(self):
    with connection.cursor() as cursor:
        # 7. UPDATE = roomRate
        # Implement a constraint using the check statement
        # Provide an interface for the user to specify some input for the update operation - User picks roomType!
        # Some input values would successfully satisfy a constraint while others would fail
        # Provide an interface for the user to display the relation relation after the operation
        # Update roomRate and ItemID with user's input
        cursor.execute("Update room2 Set roomRate = '0234' Where roomType = 'Basketball'")

def my_sql_query_15(self):
    with connection.cursor() as cursor:
        # 7. UPDATE = equipmentRate
        cursor.execute("Update Equipment_checkIn_reserveOrcancel_return1 Set EquipRate = '0123' Where EquipType = '0123'")
