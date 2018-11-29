import neighborhood
import algorithms
import random

def alg_hillie(self, neighborhood):
    """
    Hill Climber algorithms.
    """
    current = neighborhood.get_total_costs()
    for cable_1 in neighborhood.cables:
        house = cable_1.house
        battery = cable_1.battery
        cable_2 = random.choice(neigborhood.cables)
        if cable_1 == cable_2:
            # WEET NIET OF PASS WERKT
            pass
        else:
            neighborhood.disconnect(house, battery)
            neighborhood.connect(house, cable_2.battery)
            neighborhood.connect(cable_2.house, battery)
            new = neighborhood.get_total_costs()
 
        if new <= current:
            current = new
        else:
            current = current


        neighborhood.connect()
        new = SWAP 2 houses
        new.neighborhood.get_total_costs()
        check if new is > current
        if yes:
            current == new
        else:
            current == current
