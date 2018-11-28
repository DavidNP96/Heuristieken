## contains all algorithms for testing

from neighborhood import Neighborhood

def upper_bound(neighborhood):
    """
    Returns the neighborhoods upper bound by connecting
    each house to furthest battery.
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

    total_costs = neighborhood.get_total_costs()

    neighborhood.disconnect_all()

    return total_costs

def lower_bound(neighborhood):
    """
    Returns the neighborhoods lower bound by connecting
    each house to closest battery.
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

    total_costs = neighborhood.get_total_costs()

    neighborhood.disconnect_all()

    return total_costs

def simple_connect(neighborhood):
    """
    Connects each house to closest battery until battery's capacity is used.
    """

    close_battery = neighborhood.batteries[0]

    # MAKE VICINITY LIST FOR BATTERIES + USE FOR LOOP + MAKE FUNCTION

    # find closest battery for each house and then connect
    for house in neighborhood.houses:
        distance = float("inf")
        for battery in neighborhood.batteries:
            # only check for distance if battery has enough remainder
            if battery.remainder > house.output:
                current_distance = neighborhood.cal_distance(house, battery)
                if current_distance < distance:
                    distance = current_distance
                    close_battery = battery
        neighborhood.connect(house, close_battery)

    total_costs = neighborhood.get_total_costs()

    return total_costs

def get_vicinity(neighborhood):
    """
    Returns list of house ids for each battery.
    Each battery is different index in outer list.
    """

    close_battery = neighborhood.batteries[0]

    # initialize list to store house ids for each battery
    vicinity_list = [[] for i in range(len(neighborhood.batteries))]

    # add houses to list at index of closest battery
    for house in neighborhood.houses:
        # reset distance
        distance = float("inf")
        for battery in neighborhood.batteries:
            # check for closest batttery to each house
            current_distance = neighborhood.cal_distance(house, battery)
            if current_distance < distance:
                distance = current_distance
                close_battery = battery
        # add house to closest battery in list - OR ADD HOUSE ID?
        vicinity_list[close_battery.id].append(house)

    return vicinity_list



def output_priority_connect(neighborhood):
    """
    Connect function that prioritizes houses with low outputs in connecting
    to closest batteries.
    """

    # get list of closest houses per battery and sort
    vic_list = vicinity_list(neighborhood)

    sorted_list = selection_sort(vic_list)


if __name__ == "__main__":
    neighborhood1 = Neighborhood("wijk1")
    neighborhood2 = Neighborhood("wijk2")
    neighborhood3 = Neighborhood("wijk3")

    print(f"wijk1 lower bound: {lower_bound(neighborhood1)}")
    print(f"wijk2 lower bound: {lower_bound(neighborhood2)}")
    print(f"wijk3 lower bound: {lower_bound(neighborhood3)}")

    print(f"wijk1 simple connect: {simple_connect(neighborhood1)}")
    print(f"wijk2 simple connect: {simple_connect(neighborhood2)}")
    print(f"wijk3 simple connect: {simple_connect(neighborhood3)}")


    print(f"wijk1 vicinity: {get_vicinity(neighborhood1)}")
