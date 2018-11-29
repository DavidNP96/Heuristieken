class Battery(object):
    """Class containing info on battery"""
    def __init__(self, x_location, y_location, capacity, id):
        self.x_location = int(x_location)
        self.y_location = int(y_location)
        self.capacity = float(capacity)
        self.id = id

        self.remainder = self.capacity



        # Pas dit aan voor variabele prijs!
        self.price = 5000

    def move_to(self, new_x_location, new_y_location):
        self.x_location = new_x_location
        self.y_location = new_y_location
