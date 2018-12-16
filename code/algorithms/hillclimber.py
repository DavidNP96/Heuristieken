import random
from copy import deepcopy
import pandas as pd

def hillclimber(neighborhood, iterations):
    """
    Hill Climber algorithms.
    """

    current_costs = neighborhood.get_total_costs()
    plot_list = []
    plot_list.append(current_costs)
    for i in range(iterations):
        swap_succes = False

        while swap_succes != True:
            cable_1 = random.choice(neighborhood.cables)
            cable_2 = random.choice(neighborhood.cables)

            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()

        # swap back if price has not become lower
        if new_costs <= current_costs:
            current_costs = new_costs
        else:
            neighborhood.swap_connection(neighborhood.cables[-1], neighborhood.cables[-2])
        plot_list.append(current_costs)

    df = pd.DataFrame(plot_list)
    df.to_csv("hill_results.csv")
