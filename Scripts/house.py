class House(object):
    """Class containing info on house"""
    def __init__(self, x_location, y_location, output, id):
        self.x_location = x_location
        self.y_location = y_location
        self.output = float(output)
        self.id = id
        self.battery_id = None
        self.connected = False
