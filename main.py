import os
import sys

from matplotlib import pyplot as plt
import pandas as pd

import code.algorithms.greedy as g
import code.algorithms.hillclimber as h
import code.algorithms.kmeans as k
import code.algorithms.sim_annealing as sa

from code.classes.neighborhood import Neighborhood

import code.helpers.plots as pt
import code.helpers.upper_lower as uplow
import code.helpers.randoms as ran


def main():
    """ Main function

    This function can be used to get the outcomes of all the algorithms.
    """
    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")

    ran.random_connect(wijk1)
    random1 = wijk1.get_total_costs()

    ran.random_connect(wijk2)
    random2 = wijk1.get_total_costs()

    ran.random_connect(wijk3)
    random3 = wijk1.get_total_costs()

    g.greedy(wijk1)
    greedy1 = wijk1.get_total_costs()

    g.greedy(wijk2)
    greedy2 = wijk2.get_total_costs()

    g.greedy(wijk3)
    greedy3 = wijk3.get_total_costs()

    h.hillclimber(wijk1, 10000)
    greedyhill1 = wijk1.get_total_costs()

    h.hillclimber(wijk2, 10000)
    greedyhill2 = wijk2.get_total_costs()

    h.hillclimber(wijk3, 10000)
    greedyhill3 = wijk3.get_total_costs()

    g.greedy(wijk1)
    sa.sim_an_exp(wijk1, 500, 0.01, 10000)
    greedysim1 = wijk1.get_total_costs()

    g.greedy(wijk2)
    sa.sim_an_exp(wijk2, 500, 0.01, 10000)
    greedysim2 = wijk2.get_total_costs()

    g.greedy(wijk3)
    sa.sim_an_exp(wijk3, 500, 0.01, 10000)
    greedysim3 = wijk3.get_total_costs()

    # random + greedy + hillclimber
    wijk1.disconnect_all()
    ran.random_locations(wijk1)
    g.greedy(wijk1)
    h.hillclimber(wijk1, 10000)
    ran_gr_hill1 = wijk1.get_total_costs()

    wijk2.disconnect_all()
    ran.random_locations(wijk2)
    g.greedy(wijk2)
    h.hillclimber(wijk2, 10000)
    ran_gr_hill2 = wijk2.get_total_costs()

    wijk1.disconnect_all()
    ran.random_locations(wijk3)
    g.greedy(wijk3)
    h.hillclimber(wijk3, 10000)
    ran_gr_hill3 = wijk3.get_total_costs()

    # kmeans + greedy + hillclimber
    wijk1.disconnect_all()
    k.kmeans(wijk1, 10000)
    g.greedy(wijk1)
    h.hillclimber(wijk1, 10000)
    k_gr_hill1 = wijk1.get_total_costs()

    wijk2.disconnect_all()
    k.kmeans(wijk2, 10000)
    g.greedy(wijk2)
    h.hillclimber(wijk2, 10000)
    k_gr_hill2 = wijk2.get_total_costs()

    wijk3.disconnect_all()
    k.kmeans(wijk3, 10000)
    g.greedy(wijk3)
    h.hillclimber(wijk3, 10000)
    k_gr_hill3 = wijk3.get_total_costs()

    print(f"Wijk 1: \n"
          f"Costs of random:                                   {random1}\n"
          f"Costs of greedy:                                   {greedy1}\n"
          f"Costs of greedy + hillclimber:                     {greedyhill1}\n"
          f"Costs of greedy + simmulated annealing:            {greedysim1}\n"
          f"Costs of random placement + greedy + hillclimber:  {ran_gr_hill1}\n"
          f"Costs of k-means + greedy + hillclimber:           {k_gr_hill1}\n")

    print(f"Wijk 2: \n"
          f"Costs of random:                                   {random2}\n"
          f"Costs of greedy:                                   {greedy2}\n"
          f"Costs of greedy + hillclimber:                     {greedyhill2}\n"
          f"Costs of greedy + simmulated annealing:            {greedysim2}\n"
          f"Costs of random placement + greedy + hillclimber:  {ran_gr_hill2}\n"
          f"Costs of k-means + greedy + hillclimber:           {k_gr_hill2}\n")

    print(f"Wijk 3: \n"
          f"Costs of random:                                   {random3}\n"
          f"Costs of greedy:                                   {greedy3}\n"
          f"Costs of greedy + hillclimber:                     {greedyhill3}\n"
          f"Costs of greedy + simmulated annealing:            {greedysim3}\n"
          f"Costs of random placement + greedy + hillclimber:  {ran_gr_hill3}\n"
          f"Costs of k-means + greedy + hillclimber:           {k_gr_hill3}")

if __name__ == "__main__":
    main()
