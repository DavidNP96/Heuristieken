# create a grid

import csv
import matplotlib.pyplot as plt
import numpy as np

INPUT_CSV = "wijk1_huizen.csv"

with open('wijk1_huizen.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    xas = []
    yas = []
    max_output= []
    for row in reader:
        xas.append(int(row["x"]))
        yas.append(int(row["y"]))
        max_output.append(row["max. output"])
    print(xas)
    print(yas)

plt.xlabel('x')
plt.ylabel('y')
plt.title('SmartGrid')
plt.scatter(xas, yas)
plt.show()
