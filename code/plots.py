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

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for cable in neighborhood.cables:
        plt.plot([cable.house.x_location, cable.house.x_location],
            [cable.house.y_location, cable.battery.y_location],colors[cable.battery.id])
        plt.plot([cable.house.x_location, cable.battery.x_location],
            [cable.battery.y_location, cable.battery.y_location],colors[cable.battery.id])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SmartGrid')
    for house in neighborhood.houses:
        plt.scatter(house.x_location, house.y_location,  c= colors[house.battery_id] ,s=30, marker=r'^', zorder=8)
    for battery in neighborhood.batteries:
        plt.scatter(battery.x_location, battery.y_location, c = colors[battery.id],s=350, marker=r'1',zorder=10)
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
