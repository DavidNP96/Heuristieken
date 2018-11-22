import csv
import matplotlib.pyplot as plt
import numpy as np
from house import House
from battery import Battery
from cable import Cable

# selects proper csv file
INPUT_CSV = "wijk1_huizen.csv"
BATTERIES_TXT = "wijk1_batterijen.txt"


class Neighborhood(object):
    """Neighborhood class containing grid and connect function"""
    def __init__(self):
        GRID_SIZE = 50
        TOTAL_HOUSES = 50
        TOTAL_BATTERIES = 5

        self.houses = self.load_houses()
        self.battery_list = self.load_batteries()
        self.cable_list = []

    def load_houses(self):
        # opens csv and creates a reader
        with open(INPUT_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # initialize return list
            houses = []

            # creates house objects
            for row in reader:
                x_location = int(row["x"])
                y_location = int(row["y"])
                output = row["max. output"]
                house = House(x_location, y_location, output)
                houses.append(house)
            return(houses)



    def load_batteries(self):
        """
        creates list of battery objects
        """
        # opens proper battery reads only appropriate lines
        with open(BATTERIES_TXT, "r") as f:
            next(f)
            text = f.readlines()

            # list which will contain all battery objects
            batteries = []

            # creates out of every row a batterie object and puts them in list
            for row in text:
                row = row.strip("\n")
                x, y, cap = row.split()
                x = int(x.strip("[ ,"))
                y = int(y.strip("]"))
                battery = Battery(x, y, cap)
                batteries.append(battery)
            return(batteries)

    def connect(house, battery):
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)
        pass

    def get_cable_length():

        total_length = 0

        for cable in cable_list:
            total_length += cable.length

        return total_length

        pass

    def get_cable_costs():

        cable_costs = 0

        for cable in cable_list:
            cable_costs += cable.price

        return cable_costs

        pass
    def get_total_costs():

        cable_costs = 0
        battery_costs = 0

        for cable in cable_list:
            cable_costs += cable.price

        for battery in battery_list:
            battery_costs += battery.price

        total_costs = cable_costs + battery_costs

        return total_costs

        pass

    def visualize():
        x = []
        y = []
        for house in self.houses:
            x.append(house["x_location"])
            y.append(house["y_location"])
        print(x)
        print(y)


if __name__ == "__main__":
    neighborhood = Neighborhood()
