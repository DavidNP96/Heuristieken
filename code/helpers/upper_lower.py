def upper_bound(neighborhood):
    """
    Returns the neighborhoods upper bound by connecting each house to furthest
    battery without considering the capacity of the batteries.
    """

    for house in neighborhood.houses:
        distance = 0
        for battery in neighborhood.batteries:
            current_distance = neighborhood.cal_distance(house, battery)
            if current_distance > distance:
                distance = current_distance
                far_battery = battery
        neighborhood.connect_unlimited(house, far_battery)

    total_costs = neighborhood.get_total_costs()
    # neighborhood.disconnect_all()

    return total_costs

def lower_bound(neighborhood):
    """
    Returns the neighborhoods lower bound by connecting each house to closest
    battery without considering the capacity of the batteries.
    """

    for house in neighborhood.houses:
        distance = float("inf")
        for battery in neighborhood.batteries:
            current_distance = neighborhood.cal_distance(house, battery)
            if current_distance < distance:
                distance = current_distance
                close_battery = battery
        neighborhood.connect_unlimited(house, close_battery)

    total_costs = neighborhood.get_total_costs()
    # neighborhood.disconnect_all()

    return total_costs
