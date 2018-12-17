import csv
import matplotlib.pyplot as plt

file = "siman_results.csv"

with open(file, "r") as f:
        next(f)
        text = f.readlines()

x = []
y = []

for point in text:
    point = point.strip("\n")
    x_point, y_point = point.split(",")
    x.append(int(x_point))
    y.append(int(y_point))

plt.plot(x,y)
plt.show()
