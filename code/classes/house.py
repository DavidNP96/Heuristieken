class House(object):
    """House class.

    Representation of a house in neighborhood.
    """

    def __init__(self, x_location, y_location, output, id):
        """Initializes house.

        Initialize house object with needed information.
        """
        self.x_location = int(x_location)
        self.y_location = int(y_location)
        self.output = float(output)
        self.id = id
        self.battery_id = None
        self.cable_id = None
        self.connected = False

        # moet deze blijven??
        self.nearest_battery_ids = []

    def get_shortest_distance(self, battery_list):
        """
        Sets the distance to the closest battery
        """

        distance_list = []

        distance_list = self.get_distance_list(battery_list)

        return min(distance_list)

    def get_nearest_batteries(self, battery_list):
        """Get nearest batteries.

        Returns list of nearest batteries for all houses.
        """
        if battery_list is None:
            print("Battery list empty")
            return 1

        distance_list = self.get_distance_list(battery_list)

        nearest_battery_ids = [None] * len(battery_list)
        for i in range(len(battery_list)):
            nearest_battery_ids[i] = battery_list[i].id

        # bubble sort using smallest to large distance list to sort battery list
        for i in range(len(battery_list) - 1, 0, -1):
            for j in range(i):

                if distance_list[j] > distance_list[j + 1]:
                    temp_battery_id = nearest_battery_ids[j]
                    temp_distance = distance_list[j]

                    nearest_battery_ids[j] = nearest_battery_ids[j + 1]
                    distance_list[j] = distance_list[j + 1]

                    nearest_battery_ids[j + 1] = temp_battery_id
                    distance_list[j + 1] = temp_distance

        self.nearest_battery_ids = nearest_battery_ids

        return self.nearest_battery_ids

    def get_distance_list(self, battery_list):
        """Gets distance list.

        Returns list with all distances from the houses to the batteries.
        """
        distance_list = []

        for battery in battery_list:
            x_distance = abs(battery.x_location - self.x_location)
            y_distance = abs(battery.y_location - self. y_location)
            distance =  x_distance + y_distance
            distance_list.append(distance)

        return distance_list
