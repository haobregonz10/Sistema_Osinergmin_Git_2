import sqlite3
from sqlite3 import Error

def create_connection_temp():

    try:
        conn = sqlite3.connect('DATABASEAPPTEMP.db')
        return conn
    except Error as e:
        print("Error connecting to db: " + str(e))