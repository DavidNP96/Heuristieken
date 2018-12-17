import os
import sys
import csv

from code.classes.house import House
from code.classes.battery import Battery
from code.classes.cable import Cable


class Neighborhood(object):
    """Neighborhood class.

    Contains attributes and methods to setup, modify and
    use a neighborhood.
    """

    def __init__(self, neighborhood):
        """Initialize neighborhood.

        Create houses and batteries and make a list for the cables.
        """
        self.houses = self.load_houses(f"{neighborhood}_huizen.csv")
        self.batteries = self.load_batteries(f"{neighborhood}_batterijen.txt")
        self.cables = []

    def load_houses(self, input_csv):
        """Load houses.

        Creates list of house objects.
        """
        abspath = os.path.abspath(__file__)
        abspath = os.path.dirname(abspath)
        abspath = os.path.dirname(abspath)
        abspath = os.path.dirname(abspath)
        abspath = os.path.join(abspath, "data")
        abspath = os.path.join(abspath, input_csv)

        with open(abspath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            houses = []
            id = 0
            for row in reader:
                x_location = int(row["x"])
                y_location = int(row["y"])
                output = row["max. output"]
                house = House(x_location, y_location, output, id)
                houses.append(house)
                id += 1

            return(houses)

    def load_batteries(self, input_txt):
        """Load batteries.

        Creates list of battery objects.
        """
        abspath = os.path.abspath(__file__)
        abspath = os.path.dirname(abspath)
        abspath = os.path.dirname(abspath)
        abspath = os.path.dirname(abspath)
        abspath = os.path.join(abspath, "data")
        abspath = os.path.join(abspath, input_txt)

        with open(abspath, "r") as f:
            next(f)
            text = f.readlines()
            batteries = []
            id = 0
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
        """Calculates distance.

        Returns distance between specific house and battery.
        """
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)
        total_distance = x_distance + y_distance

        return total_distance

    def connect(self, house, battery):
        """Connect house and battery.

        Connects if enough capacity is left in the battery.
        """

        if (battery.remainder - house.output < 0):
            return False

        battery.remainder = battery.remainder - house.output
        cable = Cable(house, battery)
        self.cables.append(cable)
        house.battery_id = battery.id
        house.cable_id = len(self.cables) - 1
        house.connected = True

        return True

    def disconnect(self, house, battery):
        """Disconnect house and battery.

        Disconnects specific house from battery and removes cable.
        """
        for cable in self.cables:
            if house.id == cable.house.id:
                battery.remainder += house.output
                house.battery_id = None
                house.cable_id = None
                house.connected = False
                self.cables.remove(cable)

    def connect_unlimited(self, house, battery):
        """Connects all.

        Doesn't consider capacity.
        """
        cable = Cable(house, battery)
        self.cables.append(cable)
        house.battery_id = battery.id
        house.cable_id = len(self.cables) - 1

    def disconnect_all(self):
        """Disconnects all.

        Disconnects all houses and batteries and removes cables.
        """
        self.cables = []

        for house in self.houses:
            house.battery_id = None
            house.cable_id = None
            house.connected = False

        for battery in self.batteries:
            battery.remainder = battery.capacity

    def get_cable_length(self):
        """Calculates cable length.

        Returns the total length of all cables.
        """
        total_length = 0
        for cable in self.cables:
            total_length += cable.length

        return total_length

    def get_cable_costs(self):
        """Calculate cable costs.

        Returns the total costs for all cables.
        """
        cable_costs = 0
        for cable in self.cables:
            cable_costs += cable.costs

        return cable_costs

    def get_total_costs(self):
        """Calculate total costs.

        Returns the total costs for all cables and batteries.
        """
        battery_costs = 0
        for battery in self.batteries:
            battery_costs += battery.price

        cable_costs = self.get_cable_costs()
        total_costs = cable_costs + battery_costs

        return total_costs

    def swap_connection(self, cable_1, cable_2):
        """Swaps connections.

        Swaps two connections if possible.
        """
        if (cable_1 == cable_2):
            return False

        house_1 = self.houses[cable_1.house.id]
        house_2 = self.houses[cable_2.house.id]
        battery_1 = self.batteries[cable_1.battery.id]
        battery_2 = self.batteries[cable_2.battery.id]

        self.disconnect(house_1, battery_1)
        self.disconnect(house_2, battery_2)

        if not self.connect(house_1, battery_2):
            self.connect(house_1, battery_1)
            self.connect(house_2, battery_2)
            return False
        if not self.connect(house_2, battery_1):
            self.disconnect(house_1, battery_2)
            self.connect(house_1, battery_1)
            self.connect(house_2, battery_2)
            return False
        else:
            return True

    def get_nearest_houses(self):
        """Gets nearests houses of batteries.

        Returns list of house IDs for each battery.
        Each battery has a different index in outer list.
        """
        nearest_houses = [[] for i in range(len(self.batteries))]

        close_battery = self.batteries[0]
        for house in self.houses:
            battery.get_nearest_houses(self.houses)

            distance = float("inf")
            for battery in self.batteries:
                current_distance = self.cal_distance(house, battery)
                if current_distance < distance:
                    distance = current_distance
                    close_battery = battery
            nearest_houses[close_battery.id].append(house)

        return nearest_houses

    def get_all_nearest_batteries(self):
        """Gets all nearest batteries.

        Gets nearest battery for all houses.
        """
        for house in self.houses:
            house.get_nearest_batteries(self.batteries)
