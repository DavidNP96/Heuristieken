class Neighborhood(object):
    """Neighborhood class containing grid and connect function"""
    def __init__(self):
        constant int grid_size = 50
        constant int total_houses = 50
        constant int total_batteries = 5

        self.house_list = []
        self.battery_list = []
        self.cable_list = []

    def load_houses():
        # hier functie om huizen te laden en op te slaan in list



    def load_batteries():
        # hier functie om batterijen te laden en op te slaan in list



    def connect(house, battery):
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)

    def get_cable_length():

        total_length = 0

        for cable in cable_list:
            total_length += cable.length

        return total_length

    def get_cable_costs():

        cable_costs = 0

        for cable in cable_list:
            cable_costs += cable.price

        return cable_costs

    def get_total_costs():

        cable_costs = 0
        battery_costs = 0

        for cable in cable_list:
            cable_costs += cable.price

        for battery in battery_list:
            battery_costs += battery.price

        total_costs = cable_costs + battery_costs

        return total_costs
