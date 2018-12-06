# K Means algorithm

from copy import deepcopy
import numpy as np
import pandas
from matplotlib import pyplot as plt
import neighborhood as nb
import random

def kmeans(neighborhood, iterations):

    current_distance = 0
    for house in neighborhood.houses:
        current_distance = tot_distance + house.get_shortest_distance

    battery = random.choice(neighborhood.batteries)
    

    for house in neighborhood.houses:
        tot_distance = tot_distance + house.get_shortest_distance
     = tot_distance

    # print(nearest_bat_id)
