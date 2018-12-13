class Cable(object):
    """Cable class.

    Cable class for connections between houses and batteries.
    Calculates cable length and costs of cable.
    """

    def __init__(self, house, battery):
        """Initializes cable.

        Initializes cable object and saves house object, battery objects and
        the length and price of the cable.
        """
        PRICE = 9

        self.house = house
        self.battery = battery
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)
        self.length = x_distance + y_distance
        self.costs = self.length * PRICE
