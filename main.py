import os
import sys

from matplotlib import pyplot as plt

import code.algorithms.greedy as g
import code.algorithms.greedy_nieuw as gn
import code.algorithms.hillclimber as h
import code.algorithms.kmeans as k
import code.algorithms.kmeansCosts as kc
import code.algorithms.sim_annealing as sa
import code.algorithms.sim_annealing_new as san

from code.classes.neighborhood import Neighborhood

import code.helpers.plots as pt
import code.helpers.upper_lower as uplow
import code.helpers.randoms as ran
import code.helpers.simple_connect as simp
import code.helpers.kmax as kmax


def main():
    """ This function gives all the outcomes of the different algorithms.
    """

    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")


    g.greedy(wijk1)
    # ran.random_connect(wijk1)

    print(f"costs before: {wijk1.get_total_costs()}")


    # EXP DOES NOT WORK YET
    san.sim_an_exp(wijk1, 5000, 0.1, 10000)

    print(f"costs after: {wijk1.get_total_costs()}")
    # ran.all_random_locations(wijk1, 10)

    # g.greedy(wijk1)

    #
    # plots.batt_house_animate(wijk1)
    #
    # k.kmeans(wijk1, 10)
    #
    # # uplow.upper_bound(wijk1)
    # # # simp.simple_connect(wijk2)


    # greedy.greedy(wijk1)
    # plots.batt_house_plot(wijk1)
    # print(wijk1.get_total_costs())
    #
    # plots.batt_house_plot(wijk1)
    # print(wijk1.get_total_costs())

    # plots.batt_house_animate(wijk1)
    #
    # k.kmeans(wijk1, 10)
    #

    # plots.batt_house_animate(wijk1)
    # C = plots.batt_house_plot(wijk2)
    # D = plots.batt_house_plot(wijk3)

    #
    #
    # k.kmeans(wijk1, 10)
    #
    # # uplow.upper_bound(wijk1)
    # # # simp.simple_connect(wijk2)
    #
    # plots.batt_house_animate(wijk1)
    # # C = plots.batt_house_plot(wijk2)
    # # D = plots.batt_house_plot(wijk3)
    #
    # wijk1_up = Neighborhood("wijk1")
    # wijk2_up = Neighborhood("wijk2")
    # wijk3_up = Neighborhood("wijk3")


    #
    # # DIT IS VOOR ANIMATIE
    #     fig = plt.figure()
    #     camera = Camera(fig)
    #
    #     plots.batt_house_animate(wijk1)
    #     camera.snap()
    #
    #     for i in range(30):
    #         print(i)
    #         h.hillclimber(wijk1, 500)
    #         plots.batt_house_animate(wijk1)
    #         camera.snap()


if __name__ == "__main__":
    main()



# # DIT IS VOOR ANIMATIE
#     fig = plt.figure()
#     camera = Camera(fig)
#
#     plots.batt_house_animate(wijk1)
#     camera.snap()
#
#     for i in range(30):
#         print(i)
#         h.hillclimber(wijk1, 500)
#         plots.batt_house_animate(wijk1)
#         camera.snap()
    #
    #
    # total_costs = []
    # for i in range(10):
    #     k.kmeans(wijk1,10000)
    #     g.greedy(wijk1)
    #     #h.hillclimber(wijk1, 10000)
    #     sa.sim_annealing(wijk1)
    #     total_costs.append(wijk1.get_total_costs())
    #
    #
    # print(sum(total_costs)/len(total_costs))
    # plots.batt_house_plot(wijk1)

    #
    # lower_costs_1 = []
    # lower_costs_2 = []
    # lower_costs_3 = []
    # upper_costs_1 = []
    # upper_costs_2 = []
    # upper_costs_3 = []
    #
    # for i in range(10):
    #     k.kmeans(wijk1, 10000)
    #     k.kmeans(wijk2, 10000)
    #     k.kmeans(wijk3, 10000)
    #     kmax.kmeans_max(wijk1_up, 10000)
    #     kmax.kmeans_max(wijk2_up, 10000)
    #     kmax.kmeans_max(wijk3_up, 10000)
    #     uplow.lower_bound(wijk1)
    #     uplow.lower_bound(wijk2)
    #     uplow.lower_bound(wijk3)
    #     uplow.upper_bound(wijk1_up)
    #     uplow.upper_bound(wijk2_up)
    #     uplow.upper_bound(wijk3_up)
    #
    #     lower_costs_1.append(wijk1.get_total_costs())
    #     lower_costs_2.append(wijk2.get_total_costs())
    #     lower_costs_3.append(wijk3.get_total_costs())
    #
    #     upper_costs_1.append(wijk1_up.get_total_costs())
    #     upper_costs_2.append(wijk2_up.get_total_costs())
    #     upper_costs_3.append(wijk3_up.get_total_costs())
    #
    #
    # print(f"All lower_1: {lower_costs_1}")
    # print(f"Average lower_1: {sum(lower_costs_1)/len(lower_costs_1)}")
    # print(f"All lower_2: {lower_costs_2}")
    # print(f"Average lower_2: {sum(lower_costs_2)/len(lower_costs_2)}")
    # print(f"All lower_3: {lower_costs_3}")
    # print(f"Average lower_3: {sum(lower_costs_3)/len(lower_costs_3)}")
    #
    # print(f"All upper_1: {upper_costs_1}")
    # print(f"Average upper_1: {sum(upper_costs_1)/len(upper_costs_1)}")
    # print(f"All upper_2: {upper_costs_2}")
    # print(f"Average upper_2: {sum(upper_costs_2)/len(upper_costs_2)}")
    # print(f"All upper_3: {upper_costs_3}")
    # print(f"Average upper_3: {sum(upper_costs_3)/len(upper_costs_3)}")

        # h.hillclimber(wijk1, 10000)
        # print(f"cost after: {wijk1.get_total_costs()}")
    #
    # # plots.batt_house_animate(wijk1)
    # ran.random_connect(wijk1)
    #
    # fig = plt.figure()
    # camera = Camera(fig)
    #
    # plots.batt_house_animate(wijk1)
    # camera.snap()
    #
    # for i in range(30):
    #     print(i)
    #     h.hillclimber(wijk1, 500)
    #     plots.batt_house_animate(wijk1)
    #     camera.snap()

    # DAVID GEBRUIK DIT VOOR RUNSCHEMA
    # sim1_wijk1 = []
    # sim1_wijk2 = []
    # sim1_wijk3 = []
    # #
    # sim2_wijk1 = []
    # sim2_wijk2 = []
    # sim2_wijk3 = []
    # #
    # sim3_wijk1 = []
    # sim3_wijk2 = []
    # sim3_wijk3 = []
    #
    # for j in range(10):
    #     ran.random_connect(wijk1)
    #     ran.random_connect(wijk2)
    #     ran.random_connect(wijk3)
    #
    #     sa.sim_annealing(wijk1, 5000, 0.1, 0.0005)
    #     sa.sim_annealing(wijk2, 5000, 0.1, 0.0005)
    #     sa.sim_annealing(wijk3, 5000, 0.1, 0.0005)
    #
    #     sim1_wijk1.append(wijk1.get_total_costs())
    #     sim1_wijk2.append(wijk2.get_total_costs())
    #     sim1_wijk3.append(wijk3.get_total_costs())
    #

    #     wijk1.disconnect_all()
    #     wijk2.disconnect_all()
    #     wijk3.disconnect_all()
    #

    #
    #

    # for j in range(10):
    #     ran.random_connect(wijk1)
    #     ran.random_connect(wijk2)
    #     ran.random_connect(wijk3)


    #     sa.sim_annealing(wijk1, 5000, 0.1, 0.001)
    #     sa.sim_annealing(wijk2, 5000, 0.1, 0.001)
    #     sa.sim_annealing(wijk3, 5000, 0.1, 0.001)
    #
    #     sim2_wijk1.append(wijk1.get_total_costs())
    #     sim2_wijk2.append(wijk2.get_total_costs())
    #     sim2_wijk3.append(wijk3.get_total_costs())
    #
    #     wijk1.disconnect_all()
    #     wijk2.disconnect_all()
    #     wijk3.disconnect_all()

    #     print(j)
    #
    # for j in range(10):
    #     ran.random_connect(wijk1)
    #     ran.random_connect(wijk2)
    #     ran.random_connect(wijk3)
    #
    #     sa.sim_annealing(wijk1, 5000, 0.1, 0.005)
    #     sa.sim_annealing(wijk2, 5000, 0.1, 0.005)
    #     sa.sim_annealing(wijk3, 5000, 0.1, 0.005)
    #
    #     sim3_wijk1.append(wijk1.get_total_costs())
    #     sim3_wijk2.append(wijk2.get_total_costs())
    #     sim3_wijk3.append(wijk3.get_total_costs())
    #
    #     wijk1.disconnect_all()
    #     wijk2.disconnect_all()
    #     wijk3.disconnect_all()
    #
    #     print(j)

    #
    # print(f"average sim1 wijk1: {sum(sim1_wijk1)/10}")
    # print(f"lowest sim1 wijk1: {min(sim1_wijk1)}")
    # print(f"average sim1 wijk2: {sum(sim1_wijk2)/10}")
    # print(f"lowest sim1 wijk2: {min(sim1_wijk2)}")
    # print(f"average sim1 wijk3: {sum(sim1_wijk3)/10}")
    # print(f"lowest sim1 wijk3: {min(sim1_wijk3)}")
    #

    # print(f"average sim2 wijk1: {sum(sim2_wijk1)/10}")
    # print(f"lowest sim2 wijk1: {min(sim2_wijk1)}")

    #
    # print(f"average sim2 wijk1: {sum(sim2_wijk1)/10}")
    # print(f"lowest sim2 wijk1: {min(sim2_wijk1)}")

    # print(f"average sim2 wijk2: {sum(sim2_wijk2)/10}")
    # print(f"lowest sim2 wijk2: {min(sim2_wijk2)}")
    # print(f"average sim2 wijk3: {sum(sim2_wijk3)/10}")
    # print(f"lowest sim2 wijk3: {min(sim2_wijk3)}")
    #
    # print(f"average sim3 wijk1: {sum(sim3_wijk1)/10}")
    # print(f"lowest sim3 wijk1: {min(sim3_wijk1)}")
    # print(f"average sim3 wijk2: {sum(sim3_wijk2)/10}")
    # print(f"lowest sim3 wijk2: {min(sim3_wijk2)}")
    # print(f"average sim3 wijk3: {sum(sim3_wijk3)/10}")
    # print(f"lowest sim3 wijk3: {min(sim3_wijk3)}")
