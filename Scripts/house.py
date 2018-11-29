class House(object):
    """Class containing info on house"""
    def __init__(self, x_location, y_location, output, id):
        self.x_location = int(x_location)
        self.y_location = int(y_location)
        self.output = float(output)
        self.id = id
        self.battery_id = None

        self.connected = False


        # empty array to be filled with batteries order in closeness
        self.nearest_battery_ids = []


    def get_nearest_batteries(self, battery_list):

        if battery_list == None:
            print("Battery list empty")
            return 1

        distance_list = []
        nearest_battery_id = [None] * len(battery_list)

        for battery in battery_list:
            distance =  abs(battery.x_location - self.x_location) + abs(battery.y_location - self. y_location)

            distance_list.append(distance)

        # bubble sort using smallest to large distance list to sort battery list
        for i in range(len(battery_list) - 1):
            for j in range(len(battery_list) - 1):
                if distance_list[j] > distance_list[j + 1]:
                    swap_battery = battery_list[j]
                    battery_list[j] = battery_list[j + 1]
                    battery_list[j + 1] = swap_battery

        # make list with battery ids of nearest to furthest batteries
        for i in range(len(battery_list)):
            nearest_battery_id[i] = battery_list[i].id


        self.nearest_battery_ids = nearest_battery_ids
