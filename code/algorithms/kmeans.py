# K Means algorithm

from copy import deepcopy
import numpy as np
# import pandas
from matplotlib import pyplot as plt
import neighborhood as nb
import random
from copy import deepcopy


def kmeans(neighborhood, iterations):

    # calculate initaial total distance from houses to batteries
    current_distance = 0
    for house in neighborhood.houses:
        current_distance += house.get_shortest_distance(neighborhood.batteries)

    for i in range(iterations):

        # select random battery id
        battery = random.choice(neighborhood.batteries)

        # retreive current battery location
        current_x_loc = battery.x_location
        current_y_loc = battery.y_location

        # move battery by random amount between -5 and 5
        move_x = random.randint(-5, 5)
        move_y = random.randint(-5, 5)
        battery.move(move_x, move_y)

        # calculate new total distance from houses to batteries
        new_distance = 0
        for house in neighborhood.houses:
            new_distance = new_distance + house.get_shortest_distance(neighborhood.batteries)

        if new_distance  <= current_distance:
            current_distance = new_distance
        else:
            battery.move_to(current_x_loc, current_y_loc)
