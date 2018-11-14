class House(object):
    """Class containing info on house"""
    def __init__(self, x_location, y_location, output):
        self.x_location = x_location
        self.y_location = y_location
        self.output = output

        self.battery_id = None
