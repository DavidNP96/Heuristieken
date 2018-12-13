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

    current_costs = neighborhood.get_total_costs()
    plot_list = []
    plot_list.append(current_costs)
    temp_neighborhood = deepcopy(neighborhood)

    for i in range(iterations):
        battery = random.choice(temp_neighborhood.batteries)
        temp_neighborhood.disconnect_all()

        current_x_loc = battery.x_location
        current_y_loc = battery.y_location
        move_x = random.randint(-5, 5)
        move_y = random.randint(-5, 5)
        battery.move(move_x, move_y)

        new_costs = g.greedy(temp_neighborhood)
        hc.hillclimber(temp_neighborhood, 2500)
        new_costs = temp_neighborhood.get_total_costs()

        if new_costs  <= current_costs:
            current_costs = new_costs
            neighborhood = deepcopy(temp_neighborhood)
        else:
            battery.move_to(current_x_loc, current_y_loc)
        plot_list.append(current_costs)

    df = pd.DataFrame(plot_list)
    df.to_csv("kc_results.csv")
