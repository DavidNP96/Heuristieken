# Team Niko
# Heuristieken
# simple_connect.py

import random

def simple_connect(neighborhood):
    """
    Connects each house to closest battery until battery's capacity is used.
    """

    # disconnect all houses from batteries and find nearest batteries per house
    neighborhood.disconnect_all()
    neighborhood.get_all_nearest_batteries()

    # connect house to closest battery if possible, else second-to-closest etc.
    for house in neighborhood.houses:
        fail_count = 0
        while(neighborhood.connect(house, neighborhood.batteries[house.nearest_battery_ids[fail_count]])
              == False and fail_count < len(neighborhood.batteries)):
                fail_count += 1

                if fail_count == len(neighborhood.batteries):
                    print(f"Unable to connect house {house.id}")
                    current_cable = neighborhood.cables[0]
                    for cable in neighborhood.cables:
                        if cable.house.id == house.id:
                            current_cable = cable
                            break

                    while (neighborhood.swap_connection(current_cable,
                        random.choice(neighborhood.cables)) == False):
                        print("Trying to swap...")

                    fail_count = 0
    total_costs = neighborhood.get_total_costs()

    return total_costs
