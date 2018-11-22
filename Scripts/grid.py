# create a grid

import csv
import matplotlib.pyplot as plt
import numpy as np

INPUT_CSV = "Data/wijk1_huizen.csv"

with open(INPUT_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    x = []
    y = []
    max_output= []
    for row in reader:
        x.append(int(row["x"]))
        y.append(int(row["y"]))
        max_output.append(row["max. output"])
    print(x)
    print(y)

# plots house position in grid for visualization and control
plt.xlabel('x')
plt.ylabel('y')
plt.title('SmartGrid')
plt.scatter(x, y)
plt.show()
