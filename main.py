import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(directory, "data"))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from neighborhood import Neighborhood
import plots
import upper_lower as uplow
import hillclimber as h
import randoms as ran
import simple_connect as simp
<<<<<<< HEAD
import kmeans as k
import sim_annealing as sa
# from celluloid import Camera
=======
from celluloid import Camera
from matplotlib import pyplot as plt
>>>>>>> c1b34f927339d7438ac7c774b3e3972fa97c8a83

def main():
    #
    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")
    #
    # batt_house_plot(wijk)
    # k.kmeans(wijk1)
    # batt_house_plot()

    # uplow.upper_bound(wijk1)
    # simp.simple_connect(wijk2)

    # B = plots.batt_house_plot(wijk1)
    # C = plots.batt_house_plot(wijk2)
    # D = plots.batt_house_plot(wijk3)


if __name__ == "__main__":
    # main()

    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")


    ran.random_connect(wijk1)
    print(f"cost before: {wijk1.get_total_costs()}")
    plots.batt_house_plot(wijk1)
    k.kmeans(wijk1, 10000)
    simp.simple_connect(wijk1)

    # sa.sim_annealing(wijk1)
    h.hillclimber(wijk1, 10000)
    print(f"cost after: {wijk1.get_total_costs()}")
    plots.batt_house_plot(wijk1)

    # plots.batt_house_animate(wijk1)
    ran.random_connect(wijk1)

    fig = plt.figure()
    camera = Camera(fig)

    plots.batt_house_animate(wijk1)
    camera.snap()

    for i in range(30):
        print(i)
        h.hillclimber(wijk1, 500)
        plots.batt_house_animate(wijk1)
        camera.snap()
