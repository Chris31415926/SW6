# import numpy as np
# import sqlite3
# import sys
# import traceback

# dataFile = open(r"Data\data.csv", "r")
# trainingdataFile = open(r"Data\trainingdata.csv", "a+")
# line = dataFile.readline()
# stuff = 'kfk'

# def removeComma(*items): 
#     stat = ''
#     for item in items:
#         if stat:
#             stat = stat + ', ' + ''.join(item.split(','))
#         else:
#             stat = ''.join(item.split(','))
#     return stat

# def pickOutCoordinates(string):
    
#     try:
#         for section in string:
#             if section[4] is not None and section[5] is not None:
#                 # Filter the data to only include the data in the area of interest
#                 if 40.4 < float(section[4]) < 41 and -74.3 < float(section[5]) < -73.5:
#                     return section
    
#     #string = string.rpartition('(')[2]
#     #string = string.rpartition(')')[0]
    
#     #if len(string) > 20:
#         #string.len(0)
        
        
#     #return string

# trainingdataFile.write(pickOutCoordinates(line))
# #print(pickOutCoordinates(line))
# #trainingdataFile.write(removeComma('\n',example1, example2, example3))