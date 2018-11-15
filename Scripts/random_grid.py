# HAALBAARHEID
# per huis aan random batterijen connecten
# opslaan in lijst
# plot histogram met bins
from neighborhood import Neighborhood
from battery import Battery
from house import House
from cable import Cable
import random

"""
Makes an analysis of the achievablility of the upper- and lowerbound.
"""
def make_connections(self, neighborhood):
    """
    Append a connection to the connections list.
    """
    self.costs_random = []
    neighborhood.cables = []

    for i in range(50000):
        for house in neighborhood.houses:
            battery = random.choice(neighborhood.batteries)
            neighborhood.connect(house, battery)

        costs = neighborhood.get_total_costs()
        self.costs_random.append(costs)
        neighborhood.cables = []

    return self.costs_random
