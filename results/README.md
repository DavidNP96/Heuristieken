# Results

## Statespace, upper bound and lower bound
In this case there are 3 different situaties: stationary, moving, and 3 different battery types. The README of the repository contains more information about these situations.

### Stationary
#### Statespace
At first the batteries are stationary. The neighborhoods have 5 batteries and per battery it has 150 houses
it can connect to, so the number of different connections that can be made is 5^150.

#### Lower bound and upper bound
The lowerbound is the hypothetical situation where the costs of the neighborhood are the lowest possible.
All houses are connected to the closest battery. The upperbound is the opposite situation, so where all houses
are connected to the furthest battery. However, these situation will not be possible, because the capacity of 
the batteries will not be taken into account.

| Neighborhood | Lowerbound | Upperbound |
| ------------ | ---------- | ---------- |
| 1            | €53188     | €103030    |
| 2            | €45268     | €96253     |
| 3            | €42757     | €101491    |

#### Random distribution of 10000 runs
Below a histogram of the distribution 10000 runs of the random connect function is shown. 
![random_connect](https://user-images.githubusercontent.com/44001399/50083703-d93fdd00-01f4-11e9-9704-a7c48703d55a.png)

#### Distribution non random
Below a histogram of the distribution 1000 runs of the hillclimber function is shown. 
![1000_times_hillclimber _10000](https://user-images.githubusercontent.com/44001399/50116684-2a7abb80-024b-11e9-905e-8b077943d5c1.png)


#### Distribution non random
Hier komt grafiek van distributie van onze oplossingen met de simmulated annealing.

#### Scores hillclimber vs. simmulated annealing
The hillclimber has 10000 iterations. The simmualated annealing also had 10000 iterations, a Tmax of 500, and a Tmin of 0.001.
In the table below the minimum and mean of the hillclimber and the simmulated annealing for all neighborhoods are shown.

| Neighborhood | Min. HC    | Min. sim_an | Mean HC  | Mean sim_an |
| ------------ | ---------- | ----------  | -------  | ----------- |
| 1            | €56248     | €56284      | €56590.15| €56630.82   |  
| 2            | €45628     | €45664      | €46036.84| €46129.08   |  
| 3            | €43900     | €43945      | €44184.18| €44235.61   |

### Moving  
#### Statespace
In the moving situation there will still be 5^150 different possible connections between batteries and houses, but the 5 batteries can be on 2500 different locations on the grid. This makes the statespace (2500^5) * (5^150). 

#### Lower bound and upper bound
The lowerbound and upperbound is the same for all neighborhood. The lowerbound is the situation where all batteries are only one gridpoint away from the houses. The batteries will always have the same price (5 * 5000 = 25000). The cablecosts will be 150 * 9 = 1350. This gives a lowerbound of €26350. 
```
(5 * 2500) + (150 * 9) = €6350
```
The upperbound is the situation where all batteries are the furthest away from the houses as possible. This gives the total costs of 150 * 900 = 135000. The sum of the cable costs and the battery costs are €160000, which gives us the upperbound.
```
(150 * 900) + 25000 = €160000
```

We are aware of the fact that we can't use this are reference, because both bounds will never be reached. 

| Neighborhood | Lowerbound | Upperbound |
| ------------ | ---------- | ---------- |
| 1            | €6350      | €160000    |
| 2            | €6350      | €160000    |
| 3            | €6350      | €160000    |

#### Random distribution of 10000 random runs
Below a histogram of the distribution of 10000 runs of the random placement function is shown. After random placement the
greedy algorithm is used to connect the houses to batteries.
![random_placement_2](https://user-images.githubusercontent.com/44001399/50108055-94d43180-0234-11e9-965e-08b97089f987.png)


#### Distribution non random
Hier komt grafiek van distributie van onze oplossingen met k means, hillclimber en simmulated annealing. 

### Different battery types
#### Statespace
In the last situation there will be 3 different battery types. The 3 different types of batteries can be on 2500 different positions on the grid, but not on the same position as another battery. Also, there can be as many batteries as you want. So all the grid point have the posibility to have a battery on it. There are 2500 grid points and 150 houses, so the 150 have 2500 possible points to connect to. These two components together give the following statespace: (3^2500!) * 2500^150.

#### Lower bound and upper bound
The moving lowerbound and upperbound are listed in the table below. This is the same for all neighborhoods. The battery with the best price capacity ratio is the most expensive one and has a capacity of 1800. We divided 7500 (the total output of all houses in one neighborhood) by 1800 which gives 4 batteries of this types and a remainder of 300 as output of houses. This can be satisfied by the cheapest battery, which costs 900. This makes the total costs 8100. We assume that all houses are only 1 gridpoint away from the batteries. The cost of one cablegrid is 9, which makes the total cable costs 1350. The lowerbound will be 9450.
```
(4 * 1800) + 900 + (150 * 9) = €9450
```

For the upperbound all houses have their own battery. All these batteries are the most expensive type (1800) and are on the furthest possible location (100 gridpoints) from the houses. This gives the total cabelcosts of 900 per house. The upperbound will be €405000.
```
(1800 + 900) * 150 = €405000
```
Also in this case we are aware of the fact that we can't use this are reference, because both bounds will never be reached. 

| Neighborhood | Upperbound | Lowerbound |
| ------------ | ---------- | ---------- |
| 1            | €405000    | €9450      |
| 2            | €405000    | €9450      |
| 3            | €405000    | €9450      |

#### Results
We didn't have enough time to execute our ideas for this part of the case. That's why this part doesn't contain results.

## Making statespace smaller

When running the hillclimber or simulated annealing our aim is to make shure that all the houses are connected as efficient as possible(that all the houses are connected to the closest possible battery). Right now we are trying to accomplish this by means of randomly swapping cables and storing the new connection. But this, in theory, means that we also performing a multitude of swaps which are not necessary, because some cables are allready connected to closest battery. and we wouldn't want to get rid of a cable between a house with a low output that is connected to its closest battery. 

## Simmulated Annealing coolingschemes

#### Linear simmulated annealing
![siman_lin_max80_min001_iter10000](https://user-images.githubusercontent.com/44001399/50118235-5d26b300-024f-11e9-9964-f998b0b22f6f.png)

#### Exponential simmulated annealing
![siman_exp_max500_min0001_iter10000](https://user-images.githubusercontent.com/44001399/50118397-cefefc80-024f-11e9-8690-26ffe30ce9d8.png)

## Additional results
All functions have 10000 iterations. The results of all iterations are placed in CSV files in the "csv" folder. The animations
that are made are placed in a folder in called "animations".

## Plots

### Random connected + hillclimber
![random_connect](https://user-images.githubusercontent.com/44001399/49603454-a17e9d00-f98b-11e8-8a51-9298eacbeaa2.png)

### Random connected + k-means + hillclimber
![image_after](https://user-images.githubusercontent.com/44001399/49649990-22d93c80-fa2b-11e8-9f6c-b52c8335970a.png)

### Random connected + k-means + hillclimber + simmulated annealing
![simann](https://user-images.githubusercontent.com/44001399/49603363-59f81100-f98b-11e8-815e-ef5e024c919e.png)

## What makes this case difficult?
The goal of our case is to create the “cheapest” solution to a given neighbourhood. The theoretical solution to this progress is easily thought out, because there are two components that reduces or increases the cost, namely the length of the cables and the price of the chosen battery. For the first question of our case (where the batteries are stationary) this meant that we had to find  a way to connect every house to the nearest battery (which meant that the cable costs are the lowest possible). Exactly this was done by means of our lower bound algorithm. But obviously this solution does not suffice simply because the maximum capacity isn’t taken into account when connecting. So we ran in to one and probably the main problem of our case namely the fact that the houses have different output and the batteries limited capacity, because this means that although you find the best way to connect houses to batteries, this doesn’t mean that in practice this is the best way. So because the theoretical best way to connect is not available you have no aim where to end, and because of the fact that the space state is so incredibly large it is quite impossible to actually guarantee that that we reached our goal.

We found “good” solutions to our problem by running a hill climber algorithm. But because we only had a limited amount of batteries, we could supply every house with a battery, but not in every way. And this is where capacity and different output again creates a problem, namely that when running the hill climber we couldn’t connect a house with an output too large for any battery, because the batteries are already full. So we had to swap houses between batteries to create space for that one house. This often had a negative effect on the total costs of a neighbourhood, because the swaps that are performed are random. We created a heuristics that made these swaps more efficient by making a priority list of nearest batteries which the hillclimber and simulated annealing use to select cables to swap.

Eventually we could move the batteries. A big question was where to move the batteries. But eventually that question was quickly answered by our k means algorithm which moves the batteries so that the total distance from each house to a battery is reduced over every iteration. Again output and capacity are our greatest pitfall. This is because the spots we find might be optimal to reduce total distance, so in theory reduces total cable length, but it might be that an optimal spot for a battery is in the middle of a cluster of houses with high output, which means that all those houses will not fit in the nearest battery. 

The final problem includes different types of batteries. This means that in theory you want to find the best positions with the best configuration of batteries. But again the problem is that you can’t find this solution, because the configuration of batteries might not support the most efficient clusters because the houses do not have the same output, so the cable length is not minimal.

The conclusion is that the biggest pitfall of our case is the capacity of the batteries in combination with the different outputs of the houses. so far we havent yet overcome this problem in lights of the k meanas algorithm. We want to try and resolve this problem by making the k means split the clusters so we place 2 cheaper batteries with lower capacity instead of 1 expensive battery with high capacity to see if this reduces the total costs of the neighborhood. 

