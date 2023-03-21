import datetime
import numpy as np
import sqlite3
import sys
import traceback
import time

# Function to get the data from the database, filter it and return the filtered data
def get_all_data(dbPath):
    # Connect to the database
    connection = sqlite3.connect(dbPath)
    raw_data = []
    
    # Get the data from the database
    try:
        raw_data = connection.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes').fetchall()

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
def get_all_data_datetime_converted(dbPath):
    # Connect to the database
    connection = sqlite3.connect(dbPath)
    raw_data = []
    converted_data = []
    
    # Get the data from the database
    try:
        raw_data = connection.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes').fetchall()

    # If there is an error, print the error and traceback                
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    # Close the connection and return the filtered data
    connection.close()

    # Convert the date and time to a datetime object
    for i in range(len(raw_data)):

        unix_time = raw_data[i][0] + ' ' + raw_data[i][1] + ':00'

        if(len(raw_data[i][1]) == 4):
            unix_time = raw_data[i][0] + ' ' + '0' + raw_data[i][1] + ':00'

        #convert raw_data first and second columns to datetime
        unix_time = datetime.datetime.strptime(unix_time, '%m/%d/%Y %H:%M:%S')
        #convert to unix time
        unix_time = time.mktime(unix_time.timetuple())
        converted_data.append([unix_time, raw_data[i][2], raw_data[i][3]])



    print(converted_data[0])
    return converted_data

# Function to get a specified amount of data from the database, filter it and return the filtered data
def get_n_data_datetime_converted(dbPath, amount):
    # Connect to the database
    connection = sqlite3.connect(dbPath)
    raw_data = []
    converted_data = []
    
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

    # Convert the date and time to a datetime object
    for i in range(len(raw_data)):

        unix_time = raw_data[i][0] + ' ' + raw_data[i][1] + ':00'

        if(len(raw_data[i][1]) == 4):
            unix_time = raw_data[i][0] + ' ' + '0' + raw_data[i][1] + ':00'

        #convert raw_data first and second columns to datetime
        unix_time = datetime.datetime.strptime(unix_time, '%m/%d/%Y %H:%M:%S')
        #convert to unix time
        unix_time = time.mktime(unix_time.timetuple())
        converted_data.append([unix_time, raw_data[i][2], raw_data[i][3]])



    print(converted_data[0])
    return converted_data

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


