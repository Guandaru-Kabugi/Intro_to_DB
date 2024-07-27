import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

myserver = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD,
    database = 'alx_book_store'
)
print('Dtabase Opened Successfully.')
mycursor = myserver.cursor()
def create_database():
    try:
        query = 'DROP DATABASE IF EXISTS alx_book_store'
        query2 = 'CREATE DATABASE IF NOT EXISTS alx_book_store'
        mycursor.execute(query)
        mycursor.execute(query2)
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error:
        print("Error. Failed to connect Database 'alx_book_store' Successfully.")
    finally:
        mycursor.close()
        myserver.close()
        print('Database Closed Successfully.')
        
create_database()

