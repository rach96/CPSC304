import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./settings.py")
django.setup()


from django.db import connection
import argparse
from django.db import connection, transaction

import sqlite3
dbName = 'database.sqlite'
conn = sqlite3.connect(dbName)
curs = conn.cursor()

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def my_custom_sql(self):
    with curs as cursor:

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

def my_sql_query_1(self,string9,string999):
    with connection.cursor() as cursor:
        # 1. SELECTION QUERY = Select all the equipment with a specified type and display all tuples
        # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
        # NOTE = replace BASKETBALL with whatever the user inputs
        # string = SELECT * FROM Equipment_checkIn_reserveOrcancel_return1 WHERE EquipType ='Basketball'"

        string = "SELECT"
        string05 = string9 #"*"                                                             #user-selected
        string1 = " FROM Equipment_checkIn_reserveOrcancel_return1"                         #user-selected????
        string2 = " WHERE EquipType = "
        string3 = string999 #" 'BasketBall'"                                                #user-selected
        string += string05
        string += string1
        string += string2
        string += string3

        cursor.execute(string)

def my_sql_query_2(self,string9,string999):
    with connection.cursor() as cursor:
        # 1. SELECTION QUERY = Select all the rooms with a specified type and display all tuples
        # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
        # NOTE = replace 'Large Gym Room' with whatever the user input
        #cursor.execute("SELECT * FROM room1 WHERE roomType = 'Large Gym Room'")

        string = "SELECT"
        string05 = string9                                #user-selected
        string1 = " FROM room1"
        string2 = " WHERE RoomType = "
        string3 = string999                               #user-selected
        string += string05
        string += string1
        string += string2
        string += string3
        print("function being passed in")
        print(string)
        cursor.execute(string)

def my_sql_query_5(self):
    with connection.cursor() as cursor:
        # 2. JOIN = Get custID’s of customers who booked rooms
        # Provide an interface for the user to choose this query
        cursor.execute("SELECT cusID FROM reservedRoom INNER JOIN customer1 ON reservedRoom.customerID = customer1.cusID INNER JOIN room1 ON reservedRoom.customerID = room1.roomID")
        results = dictfetchall(cursor)
        print(results)
        return results


def my_sql_query_6(self):
    with connection.cursor() as curs:
        # curs.execute("SELECT * FROM sqlite_master WHERE type='table'")
        # curs.execute("CREATE TABLE TEST(cusName char(20) not null, cusPhoneNumber int null, cusBirthday text null)")
        # curs.execute("SELECT * FROM TEST")
        # results = dictfetchall(curs)
        # print(results)
        # return results
        # # 2. JOIN = Get custID’s and cusName's of customers who booked equipment
        # # Provide an interface for the user to choose this query
        curs.execute("SELECT cusID, cusName FROM Equipment_checkIn_reserveOrcancel_return2 INNER JOIN customer1 ON Equipment_checkIn_reserveOrcancel_return2.EquipCustID = customer1.cusID")
        results = dictfetchall(curs)
        print(results)
        return results


def my_sql_query_7(self):
    with connection.cursor() as cursor:
        # 3. DIVISION = Get all customers who reserved every equipment (change the sql file so that this is the case!)
        # Provide an interface for the user to choose this query
        #cursor.execute("SELECT c1.cusID FROM customer1  c1 WHERE NOT EXISTS ((SELECT e1.EquipID FROM Equipment_checkIn_reserveOrcancel_return2  e1) EXCEPT (SELECT e3.EquipID FROM Equipment_checkIn_reserveOrcancel_return2  e3, customer1  c1 WHERE E3.EquipCustID = c1.cusID))")
        cursor.execute("SELECT c1.cusID FROM customer1  c1 WHERE NOT EXISTS (SELECT * FROM Equipment_checkIn_reserveOrcancel_return2  e1 WHERE NOT EXISTS (SELECT * FROM customer1 c2 WHERE e1.EquipCustID = c1.cusID and e1.EquipCustID = c2.cusID))")
        results = dictfetchall(cursor)
        print(results)
        return results


def my_sql_query_8(self):
    with connection.cursor() as cursor:
        # 4. AGGREGATION = Total # of rooms booked during the week for all customers
        cursor.execute("SELECT Count(*) FROM reservedRoom")
        results = dictfetchall(cursor)
        print(results)
        return results


def my_sql_query_9(self):
    with connection.cursor() as cursor:
        # 4. AGGREGATION = Total # of equipment booked during the week for all customers
        cursor.execute("SELECT Count(*) FROM Equipment_checkIn_reserveOrcancel_return2")
        results = dictfetchall(cursor)
        print(results)
        return results

def my_sql_query_10(self):
    with connection.cursor() as cursor:
        # 5. NESTED AGGREGATION = average for each group and then finds either the minimum or maximum across all those averages
        # MAX(Average equipment rate for each equipment type)
        cursor.execute(
            "SELECT MAX(AverageByType) FROM (SELECT AVG(equipRate) AS AverageByType FROM Equipment_checkIn_reserveOrcancel_return1  e1 GROUP BY e1.equipType)")

        results = dictfetchall(cursor)
        print(results)
        return results

def my_sql_query_11(self):
    with connection.cursor() as cursor:
        # 5. NESTED AGGREGATION = Type of Equipment with the LEAST cost
        # MIN(Average equipment rate for each equipment type)
        cursor.execute(
            "SELECT MIN(AverageByType) FROM (SELECT AVG(equipRate) AS AverageByType FROM Equipment_checkIn_reserveOrcancel_return1  e1 GROUP BY e1.equipType)")

        results = dictfetchall(cursor)
        print(results)
        return results

def my_sql_query_12(self,string9,string99):
    with connection.cursor() as cursor:
        # 6. DELETE WITHOUT CASCADE = Delete a tuple in clean with a given RoomID, time, and employee ID
        # Some input values would fail the cascade specification but others would successfully follow the cascade specification
        # NOTE = replace employeeID, employeeroomID, and employeeTIME with user input
        cursor.execute(
           "DELETE FROM clean WHERE employeeID = '1234' and employeeroomID = '0234' and employeeTime = 'Monday'")

def my_sql_query_13(self,string9):
    with connection.cursor() as cursor:
        # 6. DELETE WITH CASCADE = Delete an customer
        # The member table now has the ON DELETE CASCADE restriction
        # If we delete an customer (which is also an athlete), there will be an error
        # cusID is either a cusID taken from member of athlete
        #cursor.execute("DELETE FROM customer1 WHERE cusID = '01234'")

        string = "DELETE FROM customer1 WHERE cusID"
        string05 = " = "
        string1 = string9 #"01234"  # user-selected
        string += string05
        string += string1

        print(string)
        cursor.execute(string)

def my_sql_query_14(self,string9):
    with connection.cursor() as cursor:
        # 7. UPDATE = roomRate
        # Implement a constraint using the check statement
        # Provide an interface for the user to specify some input for the update operation - User picks roomRate!
        # Some input values would successfully satisfy a constraint while others would fail (roomRate between $0 and $100)
        # Provide an interface for the user to display the relation relation after the operation
        # Update roomRate and ItemID with user's input
        #cursor.execute("Update room2 Set roomRate = '0234' Where roomType = 'Basketball'")

        string = "Update room2 Set"
        string05 = " roomRate = "
        string1 = string9 #"01234"                       # user-selected
        string2 = " Where roomType = 'Basketball'"
        string += string05
        string += string1
        string += string2

        cursor.execute(string)

#NOTE = THE QUERIES BELOW ARE EXTRA FUNCTIONS I AM CHOOSING NOT TO IMPLEMENT SINCE THEY ARE UNECESSARY FOR THE TIME BEING


# def my_sql_query_3(self):
#     with connection.cursor() as cursor:
#         # 1. PROJECTION QUERY = View the custIDs and cusNames of all customers that currently booked a room
#         # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
#         # NOTE = currently nothing is displaying, but that may be due to the data that is currently stored
#         cursor.execute("SELECT cusID, cusName FROM reservedRoom, room1, customer1 WHERE customerID = reservedRoom.customerID and room1.roomID = reservedRoom.customerID")
#
# def my_sql_query_4(self):
#     with connection.cursor() as cursor:
#         # 1. PROJECTION QUERY = View the custIDs and cusNames of all customers that currently booked equipment
#         # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
#         # EDIT THIS QUERY BUT TOO TIRED NOW
#         cursor.execute("SELECT cusID, cusName FROM Equipment_checkIn_reserveOrcancel_return2, customer1 WHERE cusID = Equipment_checkIn_reserveOrcancel_return2.EquipCustID")


# def my_sql_query_3(self):
#     with connection.cursor() as cursor:
#         # 1. SELECTION QUERY = Select all the equipment with a specified type and display EquipRate
#         # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
#         # NOTE = replace BASKETBALL with whatever the user inputs
#         cursor.execute("SELECT EquipRate FROM Equipment_checkIn_reserveOrcancel_return1 WHERE EquipType ='Basketball' ")
#
# def my_sql_query_4(self):
#     with connection.cursor() as cursor:
#         # 1. SELECTION QUERY = Select all the rooms with a specified type and display roomID
#         # Pick one query of this category and provide an interface for the user to specify the selection condition and the attributes to be returned.
#         # NOTE = replace 'Large Gym Room' with whatever the user input
#         cursor.execute("SELECT roomID FROM room1 WHERE roomType = 'Large Gym Room'")

# def my_sql_query_15(self):
#     with connection.cursor() as cursor:
#         # 7. UPDATE = equipmentRate
#         # Some input values would successfully satisfy a constraint while others would fail (EquipRate between $0 and $100)
#         cursor.execute("Update Equipment_checkIn_reserveOrcancel_return1 Set EquipRate = '0123' Where EquipType = '0123'")

