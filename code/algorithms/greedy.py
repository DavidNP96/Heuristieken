import random


def greedy(neighborhood):
    """Greedy algorithm.

    Connects random houses to closest battery until battery's capacity is used.
    """
    neighborhood.disconnect_all()
    neighborhood.get_all_nearest_batteries()

    connected = 0

    while connected < 150:
        house = random.choice(neighborhood.houses)

        while house.battery_id is not None:
            house = random.choice(neighborhood.houses)

        fail_count = 0
        connect_succes = False

        len_batt = len(neighborhood.batteries)

        # while (connect_succes == False and fail_count < len(neighborhood.batteries)):
        while not connect_succes and fail_count < len_batt:
            batt = neighborhood.batteries[house.nearest_battery_ids[fail_count]]
            if neighborhood.connect(house, batt):
                connected += 1
                connect_succes = True
            else:
                fail_count += 1

            if fail_count == len(neighborhood.batteries):
                current_cable = neighborhood.cables[0]
                for cable in neighborhood.cables:
                    if cable.house.id == house.id:
                        current_cable = cable
                        break

                random_cable = random.choice(neighborhood.cables)
                while not neighborhood.swap_connection(current_cable, random_cable):
                    random_cable = random.choice(neighborhood.cables)


                fail_count = 0

    total_costs = neighborhood.get_total_costs()

    return total_costs
