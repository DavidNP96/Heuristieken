class House(object):
    """Class containing info on house"""
    def __init__(self, x_location, y_location, output, id):
        self.x_location = x_location
        self.y_location = y_location
        self.output = float(output)
        self.id = id
        self.battery_id = None

        # empty array to be filled with batteries order in closeness
        self.nearest_batteries = []
