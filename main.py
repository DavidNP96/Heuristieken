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
import kmeans as k
from celluloid import Camera

def main():

    wijk1 = Neighborhood("wijk1")
    wijk2 = Neighborhood("wijk2")
    wijk3 = Neighborhood("wijk3")

    batt_house_plot()
    k.kmeans(wijk1)
    batt_house_plot()

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

    simp.simple_connect(wijk1)

    fig = plots.plt.figure()
    camera = Camera(fig)

    for i in range(100):
        h.hillclimber(wijk1, 100)
        plots.batt_house_plot(wijk1)
        camera.snap()

    animation = camera.animate()
    animation.save('animation.mp4')
