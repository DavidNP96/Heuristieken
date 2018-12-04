# SmartGrid
The energy problem is getting bigger and people are trying to reduce their impact on global warming. That's why people put 
solar panels on their roofs. The downside is that not all the energy gets used, so a lot is returned which reduces the 
profitability of getting solar panels. In this problem three neighborhoods are considered with 150 houses and 5 batteries. 
All houses with different power outputs and share the batteries which have a specific capacity.  
- The first part of the problem is to connect all houses to a battery. 
- Then the price of the neighborhood should be considered and optimized. 
- After this, the batteries can be moved to optimize the costs again. 
- In the last part of the problem three types of batteries with different prices and capacities are introduced. The algorithm 
should optimize the amount of batteries used, the position of the batteries, and the type of the battery.

![plaatje](http://heuristieken.nl/wiki/images/b/b7/Wijk1.png)

### Prerequisites
This code is completely written in [Python 3.7.1](https://www.python.org/downloads/release/python-371/). All the required 
packages are inside requirements.txt.
```
pip install -r requirements.txt
```

### Structure
All data is placed in the "data" folder. All python scripts are placed in the "code" folder. All results are placed in the 
"results" folder.

### Testing
The code can be tested by using:
```
python neighborhood.py
```

### Results
To find the statespace, upperbound, lowerbound and plots go to the "results" folder and to the README.

### Authors
**Team Niko**  
David Pantophlet  
Joost Vos  
Xandra Vos

