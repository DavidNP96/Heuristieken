class Battery(object):
    """
    Representation of a battery in neighborhood.
    """

    def __init__(self, x_location, y_location, capacity, id):
        """
        Initialize a battery with needed information.
        """
        self.x_location = int(x_location)
        self.y_location = int(y_location)
        self.capacity = float(capacity)
        self.id = id
        self.remainder = self.capacity

        # pas dit aan voor variabele prijs!
        self.price = 5000

    def move(self, move_x, move_y):
        """
        Moves battery.
        """
        if  (self.x_location + move_x) > 50:
            self.x_location = 50
        else:
            self.x_location = self.x_location + move_x
        if (self.ylocation + move_y > 50):
            self.y_location = 50
        else:
            self.y_location = self.ylocation + move_y

    def move_to(self, new_x_location, new_y_location):
        """
        Moves battery.
        """
        self.x_location = new_x_location
        self.y_location = new_y_location
