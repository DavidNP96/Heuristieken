# K Means algorithm

from copy import deepcopy
import numpy as np
from matplotlib import pyplot as plt
import neighborhood as nb
import random
from copy import deepcopy
import greedy as grd


def kmeans(neighborhood, iterations):

    # calculate initaial total price
    current_costs = grd.greedy(neighborhood)

    for i in range(iterations):

        # select random battery id
        battery = random.choice(neighborhood.batteries)

        # disconnect all houses
        neighborhood.disconnect_all()

        # retreive current battery location
        current_x_loc = battery.x_location
        current_y_loc = battery.y_location

        # move battery by random amount between -5 and 5
        move_x = random.randint(-5, 5)
        move_y = random.randint(-5, 5)
        battery.move(move_x, move_y)

        # calculate new total costs
        new_costs = grd.greedy(neighborhood)

        if new_costs  <= current_costs:
            current_costs = new_costs
        else:
            battery.move_to(current_x_loc, current_y_loc)
