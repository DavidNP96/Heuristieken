from copy import deepcopy
import random


def hillclimber(neighborhood, iterations):
    """ Hill Climber algorithm.

    Swaps cables and checks if the swap makes the neighborhood cheaper.
    If not, swaps back to the old situation.
    """

    current_costs = neighborhood.get_total_costs()

    for i in range(iterations):
        swap_succes = False

        while not swap_succes:
            cable_1 = random.choice(neighborhood.cables)
            cable_2 = random.choice(neighborhood.cables)

            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()

        if new_costs <= current_costs:
            current_costs = new_costs
        else:
            cable_1 = neighborhood.cables[-1]
            cable_2 = neighborhood.cables[-2]
            neighborhood.swap_connection(cable_1, cable_2)
