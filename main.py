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
from celluloid import Camera
from matplotlib import pyplot as plt

def main():

    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")

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

    animation = camera.animate()
    animation.save('animation.mp4')
