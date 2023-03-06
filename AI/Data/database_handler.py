import numpy as np
import sqlite3
import sys
import traceback

# Function to get the data from the database, filter it and return the filtered data
def get_all_data(dbPath):
    # Connect to the database
    connection = sqlite3.connect(dbPath)
    raw_data = []
    
    # Get the data from the database
    try:
        raw_data = connection.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes')

    # If there is an error, print the error and traceback                
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    # Close the connection and return the filtered data
    connection.close()
    return raw_data

# Function to get the data from the database, filter it and return the filtered data
def get_n_data(dbPath, amount):
    # Connect to the database
    connection = sqlite3.connect(dbPath)
    raw_data = []

    # Get the data from the database
    try:
        raw_data = connection.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes').fetchmany(amount)

    # If there is an error, print the error and traceback                
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    # Close the connection and return the filtered data
    connection.close()
    return raw_data


