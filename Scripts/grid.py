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

# plots house position in grid for visualization and control
plt.xlabel('x')
plt.ylabel('y')
plt.title('SmartGrid')
plt.scatter(house_x, house_y,  c="b", alpha=0.5, marker=r'^', label="Luck")
plt.plot(battery_x, battery_y, 'rs')
plt.plot()
plt.show()
