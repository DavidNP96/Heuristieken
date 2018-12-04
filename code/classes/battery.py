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

    def move_to(self, new_x_location, new_y_location):
        """
        Moves battery.
        """
        self.x_location = new_x_location
        self.y_location = new_y_location
