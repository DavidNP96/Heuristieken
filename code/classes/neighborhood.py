import csv
from house import House
from battery import Battery
from cable import Cable
import os, sys
import greedy as g
import sim_annealing as sa


class Neighborhood(object):
    """
    Neighborhood class containing attributes and methods to setup, modify and
    use a neighborhood.
    """
    def __init__(self, neighborhood):
        """
        Create houses and batteries and make a list for the cables.
        """
        self.houses = self.load_houses(f"{neighborhood}_huizen.csv")
        self.batteries = self.load_batteries(f"{neighborhood}_batterijen.txt")
        self.cables = []
        # self.nearest_houses = self.get_nearest_houses()

    def load_houses(self, input_csv):
        """
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

            # initialize houses list
            houses = []

            # set ID for every house to save in house object
            id = 0

            # creates house object and appends to houses list
            for row in reader:
                x_location = int(row["x"])
                y_location = int(row["y"])
                output = row["max. output"]
                house = House(x_location, y_location, output, id)
                houses.append(house)
                id += 1

            # return houses list
            return(houses)


    def load_batteries(self, input_txt):
        """
        Creates list of battery objects.
        """
        abspath = os.path.abspath(__file__)
        abspath = os.path.dirname(abspath)
        abspath = os.path.dirname(abspath)
        abspath = os.path.dirname(abspath)
        abspath = os.path.join(abspath, "data")
        abspath = os.path.join(abspath, input_txt)

        # opens txt file and starts reading at first battery in file
        with open(abspath, "r") as f:
            next(f)
            text = f.readlines()

            # initialize list for batteries
            batteries = []

            # set ID for every battery to save in battery object
            id = 0

            # creates battery objects and appends to batteries list
            for row in text:
                row = row.strip("\n")
                x, y, cap = row.split()
                x = int(x.strip("[ ,"))
                y = int(y.strip("]"))
                battery = Battery(x, y, cap, id)
                batteries.append(battery)
                id += 1

            # return list of batteries
            return(batteries)


    def cal_distance(self, house, battery):
        """
        Returns distance between specific house and battery.
        """

        # gets absolute x- and y-distance between battery and house
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)

        # calculates total distance between battery and house
        total_distance = x_distance + y_distance

        return total_distance

    def connect(self, house, battery):
        """
        Connects houses to batteries if enough capacity is left in battery.
        """

        # checks if enough capacity is left in battery to connect house
        if (battery.remainder - house.output < 0):

            # if not, returns false
            return False

        # updates capacity remainder of battery after house connects
        battery.remainder = battery.remainder - house.output

        # make cable object for this house and battery
        cable = Cable(house, battery)

        # append cable to cables list
        self.cables.append(cable)

        # sets cable_id and battery_id for house
        house.battery_id = battery.id
        house.cable_id = len(self.cables) - 1

        # sets connected property in object to true
        house.connected = True

        # return true if succesful
        return True

    def disconnect(self, house, battery):
        """
        Disconnects specific house from battery and removes cable.
        """

        # go to cable of the house that has to be disconnected and update info
        for cable in self.cables:
            if house.id == cable.house.id:
                battery.remainder += house.output
                house.battery_id = None
                house.cable_id = None
                house.connected = False
                self.cables.remove(cable)

    def connect_unlimited(self, house, battery):
        """
        Connects houses to batteries without considering capacity.
        """

        # create cable object
        cable = Cable(house, battery)

        # append cable to cables list
        self.cables.append(cable)

        # sets battery_id and cable_id for house
        house.battery_id = battery.id
        house.cable_id = len(self.cables) - 1


    def disconnect_all(self):
        """
        Disconnects all houses and batteries and removes cables.
        """

        # empty cables list
        self.cables = []

        # set all info back to initiation
        for house in self.houses:
            house.battery_id = None
            house.cable_id = None
            house.connected = False

        # set all capacity remainder back to full
        for battery in self.batteries:
            battery.remainder = battery.capacity

    def get_cable_length(self):
        """
        Returns the total length of all cables.
        """

        # initialize total length of cables
        total_length = 0

        # go through cables list and get length for all cables to add together
        for cable in self.cables:
            total_length += cable.length

        # return total length of cables
        return total_length


    def get_cable_costs(self):
        """
        Returns the total costs for all cables.
        """

        # initialize total costs of cables
        cable_costs = 0

        # go through cables list and get price for all cables to add together
        for cable in self.cables:
            cable_costs += cable.costs

        # return total costs of cables
        return cable_costs


    def get_total_costs(self):
        """
        Returns the total costs for all cables and batteries.
        """

        # initialize battery costs
        battery_costs = 0

        # get total cable costs
        cable_costs = self.get_cable_costs()

        # go through batteries list and get price for all batteries to add together
        for battery in self.batteries:
            battery_costs += battery.price

        # add costs of cables and batteries together
        total_costs = cable_costs + battery_costs

        # return total costs
        return total_costs


    def swap_connection(self, cable_1, cable_2):
        """
        Swaps two connections if possible.
        """

        # returns false if cables are the same
        if (cable_1 == cable_2):
            return False

        # get house objects out of houses list
        house_1 = self.houses[cable_1.house.id]
        house_2 = self.houses[cable_2.house.id]

        # get battery objects out of batteries list
        battery_1 = self.batteries[cable_1.battery.id]
        battery_2 = self.batteries[cable_2.battery.id]

        # disconnect all
        self.disconnect(house_1, battery_1)
        self.disconnect(house_2, battery_2)

        # returns false if new connection wasn't made and makes old connections
        if (self.connect(house_1, battery_2) == False):
            self.connect(house_1, battery_1)
            self.connect(house_2, battery_2)
            return False

        # returns false if new connection wasn't made and makes old connections
        if (self.connect(house_2, battery_1) == False):
            self.disconnect(house_1, battery_2)
            self.connect(house_1, battery_1)
            self.connect(house_2, battery_2)
            return False

        # returns true if both connections were made
        else:
            return True

    def get_nearest_houses(self):
        """
        Returns list of house IDs for each battery.
        Each battery is different index in outer list.
        """

        close_battery = self.batteries[0]

        # initialize list to store house ids for each battery
        nearest_houses = [[] for i in range(len(self.batteries))]

        # add houses to list at index of closest battery
        for house in self.houses:
            battery.get_nearest_houses(self.houses)

            # reset distance
            distance = float("inf")
            for battery in self.batteries:
                # check for closest batttery to each house
                current_distance = self.cal_distance(house, battery)
                if current_distance < distance:
                    distance = current_distance
                    close_battery = battery
            # add house to closest battery in list - OR ADD HOUSE ID?
            nearest_houses[close_battery.id].append(house)

        return nearest_houses


    def get_all_nearest_batteries(self):
        """
        Gets nearest battery for all houses.
        """
        # iterate through houses list and get nearest batteries
        for house in self.houses:
            house.get_nearest_batteries(self.batteries)

    # def move_battery(self, battery_id, x_location, y_location):
    #     """
    #     Asks house to move to desireed position.
    #     """
    #
    #     for batt in self.batteries:
    #         if battery_id == batt.id:
    #             batt.move_to(x_location, y_location)
    #



    def testen(self):
        """
        Function to test results.
        """
        for house in self.houses:
            house_test = house
            batt_id_test = house.battery_id
            for battery in self.batteries:
                if batt_id_test == battery.id:
                    battery_test = battery
                    return house_test, battery_test
