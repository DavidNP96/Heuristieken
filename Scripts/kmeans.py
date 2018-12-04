# K Means algorithm

from copy import deepcopy
import numpy as np
import pandas
from matplotlib import pyplot as plt
import neighborhood as nb

def kmeans(neighborhood):

    nearest_bat_id = []
    min_distances = []
    distance_list = []
    for house in neighborhood.houses:
        for battery in neighborhood.batteries:
            distance =  abs(battery.x_location - house.x_location) + abs(battery.y_location - house.y_location)
            distance_list.append(distance)
            for i, distance in enumerate(distance_list):
                min_distances.append(min(distance_list))
                nearest_bat_id.append(i)
    print(min_distances)
    print(nearest_bat_id)
