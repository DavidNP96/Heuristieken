# K Means algorithm

from copy import deepcopy
import numpy as np
import pandas
from matplotlib import pyplot as plt
import neighborhood as nb
import random
import pandas as pd
import hillclimber as hc
from copy import deepcopy
import greedy as grd


def kmeans(neighborhood, iterations):

    # calculate initaial total price
    current_costs = neighborhood.get_total_costs()

    temp_neighborhood = deepcopy(neighborhood)

    plot_list = []
    plot_list.append(current_costs)
    for i in range(iterations):

        # select random battery id
        battery = random.choice(temp_neighborhood.batteries)

        # disconnect all houses
        temp_neighborhood.disconnect_all()

        # retreive current battery location
        current_x_loc = battery.x_location
        current_y_loc = battery.y_location

        # move battery by random amount between -5 and 5
        move_x = random.randint(-5, 5)
        move_y = random.randint(-5, 5)
        battery.move(move_x, move_y)

        # calculate new total costs
        new_costs = grd.greedy(temp_neighborhood)
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
