import sqlite3

conn = sqlite3.connect('database.db')

print('Opened database successfully')

result = conn.execute('SELECT * FROM Motor_Vehicle_Collisions_Crashes')
count = 0

for row in result:
    if row[4] is not None and row[5] is not None:
        if float(row[4]) > 40.4 and float(row[4]) < 41 and float(row[5]) > -74.3 and float(row[5]) < -73.5:
            count = count + 1

print('Number of accidents in the area: ', count)

conn.close()