import csv
import matplotlib.pyplot as plt


def lineplot(file):
    with open(file, "r") as f:
            next(f)
            text = f.readlines()

    x = []
    y = []

    for point in text:
        point = point.strip("\n")
        x_point, y_point = point.split(",")
        x.append(int(x_point))
        y.append(int(y_point))

    plt.xlabel("Iterations")
    plt.ylabel("Total costs")
    plt.title("Cost improvement over 10000 runs")
    plt.plot(x,y)
    plt.show()


def batt_house_plot(neighborhood):
    """Plot batteries and houses.

    Plots all houses, batteries and cables.
    """
    batt_house_animate(neighborhood)
    plt.show()


def batt_house_animate(neighborhood):
    """Animate batteries and houses.

    Plots all houses, batteries and cables to make an animation.
    """
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    plot_cables(neighborhood, colors)

    plot_houses(neighborhood, colors)

    plot_batteries(neighborhood, colors)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SmartGrid')


def plot_cables(neighborhood, colors):
    """Plot cables.

    Plot all the cables of the neighborhood.
    """
    for cable in neighborhood.cables:
        house_x = cable.house.x_location
        house_y = cable.house.y_location
        battery_x = cable.battery.x_location
        battery_y = cable.battery.y_location
        x_points = [house_x, house_x, battery_x]
        y_points = [house_y, battery_y, battery_y]
        plt.plot(x_points, y_points, colors[cable.battery.id])


def plot_houses(neighborhood, colors):
    """Plot houses.

    Plots all the houses of the neighborhood on the grid.
    """
    for house in neighborhood.houses:
        x = house.x_location
        y = house.y_location
        plt.scatter(x, y, c= colors[house.battery_id] ,s=30, marker=r'^', zorder=8)


def plot_batteries(neighborhood, colors):
    """Plot batteries.

    Plot all the batteries of the neighborhood on the grid.
    """
    for battery in neighborhood.batteries:
        x = battery.x_location
        y = battery.y_location
        plt.scatter(x, y, c = colors[battery.id], s=350, marker=r'1',zorder=10)


def make_hist(info):
    """Make histogram.

    Make a histogram of solutions to find the distribution
    of the solutions.
    """
    plt.hist(info, bins=15, rwidth=0.8)
    plt.title("Random solution distribution")
    plt.xlabel("Total costs")
    plt.ylabel("Count")
    plt.show()
