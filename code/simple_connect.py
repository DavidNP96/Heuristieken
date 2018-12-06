# Team Niko
# Heuristieken
# simple_connect.py

def simple_connect(neighborhood):
    """
    Connects each house to closest battery until battery's capacity is used.
    """

    # disconnect all houses from batteries and find nearest batteries per house
    neighborhood.disconnect_all()
    neighborhood.get_all_nearest_batteries()

    # connect house to closest battery if possible, else second-to-closest etc.
    for house in neighborhood.houses:
        i = 0
        while(neighborhood.connect(house, neighborhood.batteries[house.nearest_battery_ids[i]])
              == False and i < len(neighborhood.batteries)):
                i += 1

                if i == len(neighborhood.batteries):
                    print(f"Unable to connect house {house.id}")
                    break
                #print(i)
                #print(f"ja, house id: {house.id}")

    total_costs = neighborhood.get_total_costs()

    return total_costs
