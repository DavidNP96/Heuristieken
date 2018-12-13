# Team Niko
# Heuristieken
# upper_lower.py

def upper_bound(neighborhood):
    """
    Returns the neighborhoods upper bound by connecting each house to furthest
    battery without considering the capacity of the batteries.
    """

    # find furthest battery for each house and then connect
    for house in neighborhood.houses:
        distance = 0
        for battery in neighborhood.batteries:
            current_distance = neighborhood.cal_distance(house, battery)
            if current_distance > distance:
                distance = current_distance
                far_battery = battery
        neighborhood.connect_unlimited(house, far_battery)

    # get total costs of neighborhood
    total_costs = neighborhood.get_total_costs()

    # # disconnect all houses and batteries
    # neighborhood.disconnect_all()

    return total_costs

def lower_bound(neighborhood):
    """
    Returns the neighborhoods lower bound by connecting each house to closest
    battery without considering the capacity of the batteries.
    """

    # find closest battery for each house and then connect
    for house in neighborhood.houses:
        distance = float("inf")
        for battery in neighborhood.batteries:
            current_distance = neighborhood.cal_distance(house, battery)
            if current_distance < distance:
                distance = current_distance
                close_battery = battery
        neighborhood.connect_unlimited(house, close_battery)

    # get total costs of neighborhood
    total_costs = neighborhood.get_total_costs()

    # disconnect all houses and batteries
    # neighborhood.disconnect_all()

    return total_costs
