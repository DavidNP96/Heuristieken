# Implement a greedy algorithm based on the simple-connect (but by choosing random, unconnected houses)
import neighborhood as n
import random


def greedy(neighborhood):
    """
    Connects random houses to closest battery until battery's capacity is used.
    """

    # disconnect all houses from batteries and find nearest batteries per house
    neighborhood.disconnect_all()
    neighborhood.get_all_nearest_batteries()

    # connect house to closest battery if possible, else second-to-closest etc

    connected = 0

    while connected < 150:
        house = random.choice(neighborhood.houses)

        while house.battery_id != None:
            house = random.choice(neighborhood.houses)

        fail_count = 0
        connect_succes = False

        while (connect_succes == False and fail_count < len(neighborhood.batteries)):

                if (neighborhood.connect(house, neighborhood.batteries[house.nearest_battery_ids[fail_count]])
                    == True):
                    connected += 1
                    connect_succes = True
                else:
                    fail_count += 1

                if fail_count == len(neighborhood.batteries):
                    # print(f"Unable to connect house {house.id}. Swapping...")
                    current_cable = neighborhood.cables[0]
                    for cable in neighborhood.cables:
                        if cable.house.id == house.id:
                            current_cable = cable
                            break

                    while (neighborhood.swap_connection(current_cable, random.choice(neighborhood.cables)) == False):
                        # print("Trying to swap...")

                        fail_count = 0
    total_costs = neighborhood.get_total_costs()

    return total_costs
