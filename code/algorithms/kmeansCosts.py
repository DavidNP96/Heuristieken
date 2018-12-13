from copy import deepcopy
import numpy as np
import random

import pandas
from matplotlib import pyplot as plt

import code.algorithms.greedy as g


def kmeans(neighborhood, iterations):
    """ K means algorithm.

    Finds the location for the batteries where the costs of the neighborhood
    are the lowest.
    """
    current_costs = g.greedy(neighborhood)
    for i in range(iterations):
        battery = random.choice(neighborhood.batteries)
        neighborhood.disconnect_all()
        
        current_x_loc = battery.x_location
        current_y_loc = battery.y_location

        move_x = random.randint(-5, 5)
        move_y = random.randint(-5, 5)
        battery.move(move_x, move_y)
        new_costs = g.greedy(neighborhood)

        if new_costs  <= current_costs:
            current_costs = new_costs
        else:
            battery.move_to(current_x_loc, current_y_loc)
