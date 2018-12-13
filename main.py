import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(directory, "data"))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "helpers"))

from neighborhood import Neighborhood
import plots
import upper_lower as uplow
import hillclimber as h
import randoms as ran
import simple_connect as simp
import kmeans as k
import kmax as kmax
import sim_annealing as sa
import greedy as g
from celluloid import Camera
from matplotlib import pyplot as plt


def main():

    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")

    # plots.batt_house_animate(wijk1)
    #
    # k.kmeans(wijk1, 10)

    # uplow.upper_bound(wijk1)
    # # simp.simple_connect(wijk2)

    # plots.batt_house_animate(wijk1)
    # C = plots.batt_house_plot(wijk2)
    # D = plots.batt_house_plot(wijk3)

    # wijk1_up = Neighborhood("wijk1")
    # wijk2_up = Neighborhood("wijk2")
    # wijk3_up = Neighborhood("wijk3")

    ran.all_random_locations(wijk1, 10000)






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


    # # DAVID GEBRUIK DIT VOOR RUNSCHEMA
    # sim1_wijk1 = []
    # sim1_wijk2 = []
    # sim1_wijk3 = []
    #
    # sim2_wijk1 = []
    # sim2_wijk2 = []
    # sim2_wijk3 = []
    #
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
    #     print(j)
    #
    #
    # for j in range(10):
    #     ran.random_connect(wijk1)
    #     ran.random_connect(wijk2)
    #     ran.random_connect(wijk3)
    #
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
    #
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
    #
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


if __name__ == "__main__":
    main()
