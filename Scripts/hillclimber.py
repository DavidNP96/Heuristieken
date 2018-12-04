import neighborhood as n
import random
from copy import deepcopy

def hillclimber(neighborhood, iterations):
    """
    Hill Climber algorithms.
    """

    current_costs = neighborhood.get_total_costs()

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
