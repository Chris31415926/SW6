# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:54:59 2023

@author: Torbjoern
"""
grid_lower_lat, grid_lower_lon = 40.540000, -74.1500000
grid_upper_lat, grid_upper_lon = 40.910000, -73.700000

# function for calculating the width and height of the squares in the grid
# Output: width and height of the square
def FindSize(grid_size):
    scale = 10000/2.9
    total_width = 14.6*scale
    total_height = 15.9*scale
    width = total_width/grid_size
    height = total_height/grid_size
    return width, height

# Function for calculating the centerpoints of the squares in the grid
# Output: Two arrays of the x and y coordinates for the center of the squares
def CalculateGrid(grid_size):
    dif_lng = grid_upper_lon - grid_lower_lon
    dif_lat = grid_upper_lat - grid_lower_lat
    
    latitudes = []
    longitudes = []
    for x in range (1, grid_size+1):
        point2 = grid_lower_lat + (2*x-1)*(dif_lat/(2*grid_size))
        for i in range(1, grid_size+1):
            point1 = grid_lower_lon + (2*i-1)*(dif_lng/(2*grid_size))
            longitudes.append(point1)
            latitudes.append(point2)
        
    return longitudes, latitudes

# Helper function for finding points within a square
# Output: two arrays of all x and y coordinates for the found points
def FindSelectedPoints(lower_x, lower_y, upper_x, upper_y, points_x, points_y):
    selectedPoints_x = []
    selectedPoints_y = []
  
    for i in range(len(points_x)):
        if (points_x[i]<lower_x or points_x[i]> upper_x or
            points_y[i]<lower_y or points_y[i]> upper_y):
            continue
        if (points_x[i]>lower_x and points_x[i]< upper_x and
            points_y[i]>lower_y and points_y[i]< upper_y):
            selectedPoints_x.append(points_x[i])
            selectedPoints_y.append(points_y[i])
   
    return selectedPoints_x, selectedPoints_y

# Helper function for finding the corners of a grid square
# Output: arrays containing x and y coordinates for the corners
def FindGridCorner(gridSize, x, y):
    dif_lng = grid_upper_lon - grid_lower_lon
    dif_lat = grid_upper_lat - grid_lower_lat

    x1 = x - (dif_lng/(2*gridSize))
    y1 = y - (dif_lat/(2*gridSize))

    x2 = x + (dif_lng/(2*gridSize))
    y2 = y + (dif_lat/(2*gridSize))

    return [x1, x2], [y1, y2]

webmercator_to_lonlat = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
# Helper function for converting webmercator into GPS coordinates
def ConvertWebmercator(lon, lat):
    x, y = webmercator_to_lonlat.transform(lon, lat)
    return x, y