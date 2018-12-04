# Team Niko
# Heuristieken
# plots.py

import matplotlib.pyplot as plt

def batt_house_plot(neighborhood):
    x_houses = []
    y_houses = []
    x_batteries = []
    y_batteries = []

    # create two list with house x and y coordinates
    for house in neighborhood.houses:
        x_houses.append(house.x_location)
        y_houses.append(house.y_location)

    # create two list with battery x and y coordinates
    for battery in neighborhood.batteries:
        x_batteries.append(battery.x_location)
        y_batteries.append(battery.y_location)

    for cable in neighborhood.cables:
        colors = {0 :'r', 1 :'b', 2 : 'y', 3 : 'g', 4 : 'm'}
        plt.plot([cable.house.x_location, cable.house.x_location],
            [cable.house.y_location, cable.battery.y_location],colors[cable.battery.id])
        plt.plot([cable.house.x_location, cable.battery.x_location],
            [cable.battery.y_location, cable.battery.y_location],colors[cable.battery.id] )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("SmartGrid")
    plt.scatter(x_houses, y_houses,  c="b", alpha=0.5, marker=r'^', label="Luck")
    plt.plot(x_batteries, y_batteries, 'rs')
    plt.show()


def make_hist(info):
    """
    Make a histogram of all the solutions to find the distribution.
    """

    plt.hist(info, bins=15, rwidth=0.8)
    plt.title("Random solution distribution")
    plt.xlabel("Total costs")
    plt.ylabel("Count")
    plt.show()
