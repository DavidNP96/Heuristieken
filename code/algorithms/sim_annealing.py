#import neighborhood as n
import random
import math
import pandas as pd


def acceptance_probability(current_costs, new_costs, temperature):
    if new_costs < current_costs:
        return 1.0
    else:
        return math.exp((current_costs - new_costs) / temperature)



def sim_annealing(neighborhood, Tmax, Tmin, cooling_rate):
    """
    Simulated annealing algorithm.
    """
    # defaults
    # Tmax = 25000
    temp = Tmax
    # Tmin = 0.1
    # cooling_rate = 0.0001
    plot_list = []


    current_costs = neighborhood.get_total_costs()
    plot_list.append(current_costs)

    while (temp > Tmin):
        swap_succes = False
        while swap_succes != True:
            cable_1 = random.choice(neighborhood.cables)
            cable_2 = random.choice(neighborhood.cables)
            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()

        # swap back if change not accepted
        if (acceptance_probability(current_costs, new_costs, temp) > random.random()):
            current_costs = new_costs
        else:
            neighborhood.swap_connection(neighborhood.cables[-1], neighborhood.cables[-2])
        plot_list.append(current_costs)

        # exponential
        temp = temp * (1 - cooling_rate)

        # linear, check if cooling is not too fast
        temp = temp - cooling_rate
        #
        # # logaritmic
        temp = log(cooling_rate * temp)


    df = pd.DataFrame(plot_list)
    df.to_csv("siman_results.csv")

if __name__ == "__main__":
    print(acceptance_probability(2, 38, 10000))
    print(acceptance_probability(2, 45, 1))
