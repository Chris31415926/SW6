import numpy as np
import sqlite3
import sys
import traceback

def get_data():
    connection = sqlite3.connect('datasetNY.db')

    raw_data = connection.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes')
    filtered_data = []

    try:
        for row in raw_data:
            if row[4] is not None and row[5] is not None:
                if float(row[4]) > 40.4 and float(row[4]) < 41 and float(row[5]) > -74.3 and float(row[5]) < -73.5:
                    filtered_data.append(row)
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    connection.close()
    return filtered_data
