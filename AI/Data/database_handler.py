import numpy as np
import sqlite3
import sys
import traceback

# Function to get the data from the database, filter it and return the filtered data
def get_data():
    # Connect to the database
    connection = sqlite3.connect('datasetNY.db')

    # Get the data from the database
    raw_data = connection.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes')
    filtered_data = []

    # Filter the data
    try:
        for row in raw_data:
            if row[4] is not None and row[5] is not None:
                # Filter the data to only include the data in the area of interest
                if 40.4 < float(row[4]) < 41 and -74.3 < float(row[5]) < -73.5:
                    filtered_data.append(row)

    # If there is an error, print the error and traceback                
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    # Close the connection and return the filtered data
    connection.close()
    return filtered_data