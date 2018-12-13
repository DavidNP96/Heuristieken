import random

import pandas as pd

import code.helpers.plots as pt
import code.algorithms.greedy as g

def random_connect(neighborhood):
    """
    Randomly connects all houses to batteries to create random distribution.
    """

    neighborhood.disconnect_all()

    # dit is niet helemaal random!!! Probeer random.choice(houses) en dan if house.battery_id != None oid
    for house in neighborhood.houses:
        unconnectable_count = 0
        battery = random.choice(neighborhood.batteries)
        connected = neighborhood.connect(house, battery)
        while (connected != True):
            battery = random.choice(neighborhood.batteries)
            unconnectable_count += 1
            if unconnectable_count > 50:
                swap_succes = neighborhood.swap_connection(random.choice(neighborhood.cables), random.choice(neighborhood.cables))
                while (swap_succes != True):
                    swap_succes = neighborhood.swap_connection(random.choice(neighborhood.cables),
                    random.choice(neighborhood.cables))
            connected = neighborhood.connect(house, battery)


def all_random_connect(neighborhood, iterations):
    """
    Makes histogram of executing random connect the given amount of times.
    """

    # Make list for all random costs retrieved
    costs_random = []

    # Execute random_connect and append costs to list for all iteration
    for i in range(iterations):
        random_connect(neighborhood)
        total_costs = neighborhood.get_total_costs()
        costs_random.append(total_costs)

    # Make histogram of all costs in list
    plots.make_hist(costs_random)


def random_locations(neighborhood):
    """
    Puts batteries at random locations.
    """

    for battery in neighborhood.batteries:
        x_location = random.randint(-50, 50)
        y_location = random.randint(-50, 50)
        battery.move_to(x_location, y_location)


def all_random_locations(neighborhood, iterations):
    """
    Makes histogram of costs after greedy connect algorithm after random
    battery placement.
    """

    costs_random = []

    # Execute random_connect and append costs to list for all iterations
    for i in range(iterations):
        random_locations(neighborhood)
        g.greedy(neighborhood)
        total_costs = neighborhood.get_total_costs()
        costs_random.append(total_costs)

    # Write costs list to CSV file
    df = pd.DataFrame(costs_random)
    df.to_csv("results_random.csv")

    # Make histogram of all costs in list
    pt.make_hist(costs_random)