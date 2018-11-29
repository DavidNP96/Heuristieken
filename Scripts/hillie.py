import neighborhood
import algorithms
import random

def alg_hillie(neighborhood):
    """
    Hill Climber algorithms.
    """
    current = neighborhood.get_total_costs()
    # neighborhood.batt_house_plot()
    print(current)
    for i in range(500):
        for cable_1 in neighborhood.cables:
            house_1 = cable_1.house
            battery_1 = cable_1.battery
            while True:
                cable_2 = random.choice(neighborhood.cables)
                house_2 = cable_2.house
                battery_2 = cable_2.battery
                if not cable_1 == cable_2:
                    break
            neighborhood.disconnect(house_1, battery_1)
            neighborhood.disconnect(house_2, battery_2)

            neighborhood.connect(house_1, battery_2)
            neighborhood.connect(house_2, battery_1)
            new = neighborhood.get_total_costs()

            if new > current:
                neighborhood.disconnect(house_1, battery_2)
                neighborhood.disconnect(house_2, battery_1)
                neighborhood.connect(house_2, battery_2)
                neighborhood.connect(house_1, battery_1)
                print(new)
     # neighborhood.batt_house_plot()
