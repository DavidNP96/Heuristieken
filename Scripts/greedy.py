# Implement a greedy algorithm based on the simple-connect (but by choosing random, unconnected houses)
import neighborhood as n
import random


def greedy(neighborhood):
    """
    Connects random houses to closest battery until battery's capacity is used.
    """

    # disconnect all houses from batteries and find nearest batteries per house
    neighborhood.disconnect_all()
    neighborhood.get_nearest_batteries()

    # connect house to closest battery if possible, else second-to-closest etc

    connected = 0

    while connected < 150:
        house = random.choice(neighborhood.houses)

        while house.battery_id != None:
            house = random.choice(neighborhood.houses)

        i = 0
        connect_succes = False

        while (connect_succes == False and i < len(neighborhood.batteries)):

                if (neighborhood.connect(house, neighborhood.batteries[house.nearest_battery_ids[i]])
                    == True):
                    connected += 1
                    connect_succes = True
                else:
                    i += 1

                print(i)

                if i == len(neighborhood.batteries):
                    print(f"Unable to connect house {house.id}. Swapping...")
                    current_cable = neighborhood.cables[0]
                    for cable in neighborhood.cables:
                        if cable.house.id == house.id:
                            current_cable = cable
                            break

                    while (neighborhood.swap_connection(current_cable, random.choice(neighborhood.cables) == False)):
                        print("Trying to swap...")

    total_costs = neighborhood.get_total_costs()

    return total_costs
