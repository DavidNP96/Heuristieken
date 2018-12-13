import random
from copy import deepcopy

def hillclimber_testing(neighborhood, iterations):
    """
    Hill Climber algorithms.
    """

    bad_cables = []

    for cable in neighborhood.cables:
        nearest_battery_ids = cable.house.get_nearest_batteries(neighborhood.batteries)
        # print(neighborhood.batteries)
        # print(cable.house.get_nearest_batteries(neighborhood.batteries))
        # print(cable.battery.id)
        # print(nearest_battery_ids)
        if not cable.battery.id == nearest_battery_ids[0]:
            bad_cables.append(cable)

    print(len(bad_cables))



    current_costs = neighborhood.get_total_costs()

    for i in range(iterations):
        swap_succes = False

        while swap_succes != True:
            cable_1 = random.choice(bad_cables)
            cable_2 = random.choice(bad_cables)

            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()

        # swap back if price has not become lower
        if new_costs <= current_costs:
            current_costs = new_costs
        else:
            neighborhood.swap_connection(neighborhood.cables[-1], neighborhood.cables[-2])
