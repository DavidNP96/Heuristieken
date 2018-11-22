import csv
#import matplotlib.pyplot as plt
#import numpy as np
from house import House
from battery import Battery
from cable import Cable

# import random_grid
import random
import matplotlib.pyplot as plt

# selects proper csv file
# INPUT_CSV = "wijk1_huizen.csv"
# BATTERIES_TXT = "wijk1_batterijen.txt"


class Neighborhood(object):
    """
    Neighborhood class containing grid and connect function.
    """
    def __init__(self, neighborhood):

        self.houses = self.load_houses(f"Data/{neighborhood}_huizen.csv")
        self.batteries = self.load_batteries(f"Data/{neighborhood}_batterijen.txt")
        self.cables = []


    def load_houses(self, input_csv):
        """
        Opens csv and creates a reader.
        """
        with open(input_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # initialize return list
            houses = []

            id = 0
            # creates house object list and uses row for house id
            for row in reader:
                x_location = int(row["x"])
                y_location = int(row["y"])
                output = row["max. output"]
                house = House(x_location, y_location, output, id)
                houses.append(house)
                id += 1
            # print(houses)
            return(houses)


    def load_batteries(self, input_txt):
        """
        Creates list of battery objects.
        """
        # opens proper battery reads only appropriate lines
        with open(input_txt, "r") as f:
            next(f)
            text = f.readlines()

            # list which will contain all battery objects
            batteries = []

            id = 0

            # creates battery object list and uses row for battery id
            for row in text:
                row = row.strip("\n")
                x, y, cap = row.split()
                x = int(x.strip("[ ,"))
                y = int(y.strip("]"))
                battery = Battery(x, y, cap, id)
                batteries.append(battery)
                id += 1
            return(batteries)


    def cal_distance(self, house, battery):
        """
        Returns distance between house and battery.
        """
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)

        total_distance = x_distance + y_distance

        return total_distance

    def connect(self, house, battery):
        """
        Connects houses to batteries.
        """



        if (battery.remainder - house.output < 0):
            #print(battery.remainder - house.output)
            return False

        battery.remainder = battery.remainder - house.output

        cable = Cable(house, battery)

        self.cables.append(cable)

        # sets battery_id for house
        house.battery_id = battery.id

        return True

    def connect_unlimited(self, house, battery):
        """Connects houses to batteries"""

        cable = Cable(house, battery)

        self.cables.append(cable)

        # sets battery_id for house
        house.battery_id = battery.id


    def disconnect_all(self):
        """
        Disconnects all houses and batteries and removes cables.

        MAYBE ALSO FUNCTION TO DISCONNECT 1 BATTERY FROM 1 HOUSE?"""

        self.cables = []

        for house in self.houses:
            house.battery_id = None

        for battery in self.batteries:
            battery.remainder = battery.capacity

    def get_cable_length(self):
        """
        Returns the total length of all cables.
        """
        total_length = 0

        for cable in cables:
            total_length += cable.length

        return total_length


    def get_cable_costs(self):
        """
        Returns the total costs for all cables.
        """
        cable_costs = 0

        for cable in cables:
            cable_costs += cable.price

        return cable_costs


    def get_total_costs(self):
        """
        Returns the total costs for all cables and batteries.
        """
        cable_costs = 0
        battery_costs = 0

        for cable in self.cables:
            cable_costs += cable.costs

        for battery in self.batteries:
            battery_costs += battery.price

        total_costs = cable_costs + battery_costs

        return total_costs

    def upper_bound(self):
        """
        Returns the neighborhoods upper bound by connecting
        each house to furthest battery.
        """

        # find furthest battery for each house and then connect
        for house in self.houses:
            distance = 0
            for battery in self.batteries:
                current_distance = self.cal_distance(house, battery)
                if current_distance > distance:
                    distance = current_distance
                    far_battery = battery
            self.connect(house, far_battery)

        total_costs = self.get_total_costs()

        self.disconnect_all()

        return total_costs

    def lower_bound(self):
        """
        Returns the neighborhoods lower bound by connecting
        each house to closest battery.
        """

        # find closest battery for each house and then connect
        for house in self.houses:
            distance = float("inf")
            for battery in self.batteries:
                current_distance = self.cal_distance(house, battery)
                if current_distance < distance:
                    distance = current_distance
                    close_battery = battery
            self.connect(house, close_battery)

        total_costs = self.get_total_costs()

        self.disconnect_all()

        return total_costs

    def connect_random(self):
        """
        Append a connection to the connections list.
        """
        self.costs_random = []
        #self.disconnect_all()

        penalty_count = 0

        for i in range(50000):
            penalty = 0
            for house in self.houses:
                battery = random.choice(self.batteries)
                if not self.connect(house, battery):
                    count = 0
                    for battery in self.batteries:
                        count += 1
                        if battery == random.choice(self.batteries):
                            break
                        elif count == 5:
                            penalty += 900
            if penalty > 0:
                penalty_count += 1
            costs = self.get_total_costs() + penalty
            self.costs_random.append(costs)
            # print("yeeeah1")
            self.disconnect_all()
            # print("yeaah2")

        print (f"Number of incomplete connection attempts: {penalty_count}")
        return self.costs_random

    def make_hist(self, info):
        """
        Make a histogram of all the solutions to find the distribution.
        """
        plt.hist(info, bins=15, rwidth=0.8)
        plt.show()


if __name__ == "__main__":
    neighborhood1 = Neighborhood("wijk1")
    neighborhood2 = Neighborhood("wijk2")
    neighborhood3 = Neighborhood("wijk3")
    #
    # print(f"wijk1 upper bound: {neighborhood1.upper_bound()}")
    # print(f"wijk2 upper bound: {neighborhood2.upper_bound()}")
    # print(f"wijk3 upper bound: {neighborhood3.upper_bound()}")
    #
    # print(f"wijk1 lower bound: {neighborhood1.lower_bound()}")
    # print(f"wijk2 lower bound: {neighborhood2.lower_bound()}")
    # print(f"wijk3 lower bound: {neighborhood3.lower_bound()}")

    costs_random = neighborhood1.connect_random()
    neighborhood1.make_hist(costs_random)

    print(f"wijk1 simple connect: {neighborhood1.simple_connect()}")
    print(f"wijk2 simple connect: {neighborhood2.simple_connect()}")
    print(f"wijk3 simple connect: {neighborhood3.simple_connect()}")

    # print(f"simple_connect voor wijk1: {neighborhood1.simple_connect()}")
