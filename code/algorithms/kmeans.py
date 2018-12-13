from copy import deepcopy
import numpy as np
import random

from matplotlib import pyplot as plt


def kmeans(neighborhood, iterations):
    """K-means algorithm.

    Finds the location for the batteries where the total distance of the
    neighborhood are the lowest.
    """

    current_distance = 0
    for house in neighborhood.houses:
        current_distance += house.get_shortest_distance(neighborhood.batteries)

    for i in range(iterations):
        battery = random.choice(neighborhood.batteries)
        current_x_loc = battery.x_location
        current_y_loc = battery.y_location

        move_x = random.randint(-5, 5)
        move_y = random.randint(-5, 5)
        battery.move(move_x, move_y)

        new_distance = 0
        for house in neighborhood.houses:
            new_distance = new_distance + house.get_shortest_distance(neighborhood.batteries)

        if new_distance  <= current_distance:
            current_distance = new_distance
        else:
            battery.move_to(current_x_loc, current_y_loc)
