import random


def simple_connect(neighborhood):
    """
    Connects each house to closest battery until battery's capacity is used.
    """
    neighborhood.disconnect_all()
    neighborhood.get_all_nearest_batteries()

    for house in neighborhood.houses:
        fail_count = 0
        battery = neighborhood.batteries[house.nearest_battery_ids[fail_count]]
        len_batt = len(neighborhood.batteries)
        while not neighborhood.connect(house, battery) and fail_count >= len_batt:
                fail_count += 1
                battery = neighborhood.batteries[house.nearest_battery_ids[fail_count]]
                if fail_count == len_batt:
                    print(f"Unable to connect house {house.id}")
                    current_cable = neighborhood.cables[0]
                    for cable in neighborhood.cables:
                        if cable.house.id == house.id:
                            current_cable = cable
                            break

                    random_cable = random.choice(neighborhood.cables)
                    while not neighborhood.swap_connection(current_cable, random_cable):
                        print("Trying to swap...")
                        random_cable = random.choice(neighborhood.cables)

                    fail_count = 0

    total_costs = neighborhood.get_total_costs()

    return total_costs
