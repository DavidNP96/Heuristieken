class Cable(object):
    """Cable class for connections between houses and batteries.
        Calculates cable length and costs of cable."""
    def __init__(self, house, battery):
        PRICE = 9

        # calculate distance from house to battery
        x_distance = abs(house.x_location - battery.x_location)
        y_distance = abs(house.y_location - battery.y_location)
        self.length = x_distance + y_distance

        self.costs = self.length * price
