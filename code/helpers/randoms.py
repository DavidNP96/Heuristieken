import random

import pandas as pd

import code.helpers.plots as pt
import code.algorithms.greedy as g


def random_connect(neighborhood):
    """
    Randomly connects all houses to batteries to create random distribution.
    """
    neighborhood.disconnect_all()

    connected_count = 0

    while (connected_count < 150):
        house = random.choice(neighborhood.houses)
        while house.battery_id is not None:
            house = random.choice(neighborhood.houses)

        unconnectable_count = 0
        battery = random.choice(neighborhood.batteries)
        connected = neighborhood.connect(house, battery)

        while not connected:
            battery = random.choice(neighborhood.batteries)
            unconnectable_count += 1
            if unconnectable_count > 50:
                cable_1 = random.choice(neighborhood.cables)
                cable_2 = random.choice(neighborhood.cables)
                swap_succes = neighborhood.swap_connection(cable_1, cable_2)
                while not swap_succes:
                    cable_1 = random.choice(neighborhood.cables)
                    cable_2 = random.choice(neighborhood.cables)
                    swap_succes = neighborhood.swap_connection(cable_1, cable_2)
            connected = neighborhood.connect(house, battery)

        connected_count += 1


def all_random_connect(neighborhood, iterations):
    """
    Makes histogram of executing random connect the given amount of times.
    """
    costs_random = []

    for i in range(iterations):
        random_connect(neighborhood)
        total_costs = neighborhood.get_total_costs()
        costs_random.append(total_costs)

    pt.make_hist(costs_random)


def random_locations(neighborhood):
    """
    Puts batteries at random locations.
    """

    for battery in neighborhood.batteries:
        x_location = random.randint(0, 50)
        y_location = random.randint(0, 50)
        battery.move_to(x_location, y_location)


def all_random_locations(neighborhood, iterations):
    """
    Makes histogram of costs after greedy connect algorithm after random
    battery placement.
    """

    costs_random = []

    for location in range(iterations):
        random_locations(neighborhood)
        g.greedy(neighborhood)
        total_costs = neighborhood.get_total_costs()
        costs_random.append(total_costs)

    pt.make_hist(costs_random)
