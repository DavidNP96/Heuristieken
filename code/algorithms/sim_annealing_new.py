import pandas as pd
import math
import random
import decimal


def acceptance_probability(current_costs, new_costs, temperature):
    """
    AANVULLEN.
    """
    if new_costs < current_costs:
        return 1.0
    else:
        return math.exp((current_costs - new_costs) / temperature)


def sim_an_exp(neighborhood, Tmax, Tmin, iterations):
    """
    Simulated annealing algorithm using an exponential cooling scheme.

    Tries to find cheapest neighborhood. AANVULLEN.
    """

    temp = Tmax

    # set iteration number to 0 at start
    n = 0

    plot_list = []

    cooling_rate = float(Tmin/Tmax)**(1/iterations)


    while (n < iterations):

        # adjust temperature according to exponential cooling scheme
        temp = Tmax * (float(cooling_rate)**float(n))

        swap_succes = False
        while not swap_succes:
            cable_1 = random.choice(neighborhood.cables)
            cable_2 = random.choice(neighborhood.cables)
            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()
        if (acceptance_probability(current_costs, new_costs, temp) > random.random()):
            current_costs = new_costs
        else:
            cable_1 = neighborhood.cables[-1]
            cable_2 = neighborhood.cables[-2]
            neighborhood.swap_connection(cable_1, cable_2)

        plot_list.append(current_costs)
        n += 1

    df = pd.DataFrame(plot_list)
    df.to_csv("sim_an_exp_results.csv")


def sim_an_lin(neighborhood, Tmax, Tmin, iterations):
    """Simulated annealing algorithm using a linear cooling scheme.

    Tries to find cheapest neighborhood. AANVULLEN.
    """

    temp = Tmax

    # set iteration number to 0
    n = 0

    plot_list = []

    current_costs = neighborhood.get_total_costs()

    cooling_rate = (Tmax-Tmin) / iterations


    while (n < iterations):

        # adjust temperature according to exponential cooling scheme
        temp = Tmax - (n * cooling_rate)


        swap_succes = False
        while not swap_succes:
            cable_1 = random.choice(neighborhood.cables)
            cable_2 = random.choice(neighborhood.cables)
            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()
        if (acceptance_probability(current_costs, new_costs, temp) > random.random()):
            current_costs = new_costs
        else:
            cable_1 = neighborhood.cables[-1]
            cable_2 = neighborhood.cables[-2]
            neighborhood.swap_connection(cable_1, cable_2)

        plot_list.append(current_costs)
        n += 1

    df = pd.DataFrame(plot_list)
    df.to_csv("sim_an_lin_results.csv")

def sim_an_reheat(neighborhood, Tmax, Tmin, iterations):
    """
    Simulated annealing algorithm using an exponential cooling scheme.
    Uses reheating to find optimal result
    Tries to find cheapest neighborhood. AANVULLEN.
    """

    temp = Tmax

    # set iteration number to 0 at start
    n = 0

    plot_list = []

    current_costs = neighborhood.get_total_costs()
    cooling_rate = float(Tmin/Tmax)**(1/iterations)

    reheat_moment = 0.99
    reheat_factor = 0.7

    reheated = False

    while n < iterations:


        if n == iterations * reheat_moment and not reheated:
            print(f"costs before: {neighborhood.get_total_costs()}")
            n -= (n * reheat_factor)
            # print(f"n aftere: {n}")
            # print("yes")
            reheated = True


        # adjust temperature according to exponential cooling scheme
        temp = Tmax * (float(cooling_rate)**float(n))
        #
        # print(f"{n}, {temp}")

        swap_succes = False
        while not swap_succes:
            cable_1 = random.choice(neighborhood.cables)
            cable_2 = random.choice(neighborhood.cables)
            swap_succes = neighborhood.swap_connection(cable_1, cable_2)

        new_costs = neighborhood.get_total_costs()
        if (acceptance_probability(current_costs, new_costs, temp) > random.random()):
            current_costs = new_costs
        else:
            cable_1 = neighborhood.cables[-1]
            cable_2 = neighborhood.cables[-2]
            neighborhood.swap_connection(cable_1, cable_2)

        plot_list.append(current_costs)
        n += 1

    df = pd.DataFrame(plot_list)
    df.to_csv("sim_an_reheat_results.csv")

    print(f"costs after: {neighborhood.get_total_costs()}")

if __name__ == "__main__":
    print(acceptance_probability(2, 38, 10000))
    print(acceptance_probability(2, 45, 1))
