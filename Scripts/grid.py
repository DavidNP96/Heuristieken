# create a grid

import csv
import matplotlib.pyplot as plt
import numpy as np
from neighborhood import Neighborhood

INPUT_CSV = "Data/wijk1_huizen.csv"
INPUT_TEXT = "Data/wijk1_batterijen.txt"

#
with open(INPUT_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    house_x = []
    house_y = []
    max_output= []
    for row in reader:
        house_x.append(int(row["x"]))
        house_y.append(int(row["y"]))
        max_output.append(row["max. output"])
    print(house_x)
    print(house_y)

with open(INPUT_TEXT, "r") as f:
    next(f)
    text = f.readlines()

    # list which will contain all battery objects
    battery_x= []
    battery_y = []

    # creates out of every row a batterie object and puts them in list
    for row in text:
        row = row.strip("\n")
        x, y, cap = row.split()
        x = int(x.strip("[ ,"))
        y = int(y.strip("]"))
        battery_x.append(x)
        battery_y.append(y)
    print(battery_x)
    print(battery_y)

# function to draw lines between batteries and houses
# def connectpoints(x,y,p1,p2):
#     """
#     Draw connections between batteries and houses
#     """
#     for
#     x1, x2 = x[p1], x[p2]
#     y1, y2 = y[p1], y[p2]
    plt.plot([house_x, house_y], [battery_x, battery_y], "k-")

# connectpoints(x,y,0,1)
# connectpoints(x,y,2,3)

# plots house position in grid for visualization and control
plt.xlabel('x')
plt.ylabel('y')
plt.title('SmartGrid')
plt.scatter(house_x, house_y,  c="b", alpha=0.5, marker=r'^', label="Luck")
plt.scatter(battery_x, battery_y)
plt.plot()
plt.show()
