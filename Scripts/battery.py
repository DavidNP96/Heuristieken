class Battery(object):
    """Class containing info on battery"""
    def __init__(self, x_location, y_location, capacity, id):
        self.x_location = x_location
        self.y_location = y_location
        self.capacity = capacity
        self.id = id

        self.remainder = capacity



        # Pas dit aan voor variabele prijs!
        self.price = 5000
