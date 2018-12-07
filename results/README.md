# Results

## Statespace, upperbound and lowerbound
In this case there are 3 different situaties: stationary, moving, and 3 different battery types. The README of the repository contains more information about these situations.

### Stationary
#### Statespace
At first the batteries are stationary. The neighborhoods have 5 batteries and per battery it has 150 houses
it can connect to, so the number of different connections that can be made is 5^150.

#### Lowerbound and upperbound
The lowerbound is the hypothetical situation where the costs of the neighborhood are the lowest possible.
All houses are connected to the closest battery. The upperbound is the opposite situation, so where all houses
are connected to the furthest battery. However, these situation will not be possible, because the capacity of 
the batteries will not be taken into account.

| Neighborhood | Upperbound | Lowerbound |
| ------------ | ---------- | ---------- |
| 1            | €103030    | €53188     |
| 2            | €96253     | €45268     |
| 3            | €101491    | €42757     |

![random_stationary](https://user-images.githubusercontent.com/44001399/49597905-bd7b4200-f97d-11e8-9c74-5e2a9ab4fab1.png)


### Moving  
#### Statespace
In the moving situation there will still be 5^150 different possible connections between batteries and houses, but the 5 batteries can be on 2500 different locations on the grid. This makes the statespace (2500^5) * (5^150). 

#### Lowerbound and upperbound
The lowerbound and upperbound is the same for all neighborhood. The lowerbound is the situation where all batteries are only one gridpoint away from the houses. The batteries will always have the same price (5 * 5000 = 25000). The cablecosts will be 150 * 9 = 1350. This gives a lowerbound of €26350. 
```
(5 * 2500) + (150 * 9) = €6350
```
The upperbound is the situation where all batteries are the furthest away from the houses as possible. This gives the total costs of 150 * 900 = 135000. The sum of the cable costs and the battery costs are €160000, which gives us the upperbound.
```
(150 * 900) + 25000 = €160000
```

We are aware of the fact that we can't use this are reference, because both bounds will never be reached. 

| Neighborhood | Upperbound | Lowerbound |
| ------------ | ---------- | ---------- |
| 1            | €103030    | €38932     |
| 2            | €96253     | €39895     |
| 3            | €101491    | €39607     |

### Different battery types
#### Statespace
In the last situation there will be 3 different battery types. The 3 different types of batteries can be on 2500 different positions on the grid, but not on the same position as another battery. Also, there can be as many batteries as you want. So all the grid point have the posibility to have a battery on it. There are 2500 grid points and 150 houses, so the 150 have 2500 possible points to connect to. These two components together give the following statespace: (3^2500!) * 2500^150.

#### Lowerbound and upperbound
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

## What makes this case difficult?
The goal of our case is to create the “cheapest” solution to a given neighbourhood. The theoretical solution to this progress is easily thought out, because there are two components that reduces or increases the cost, namely the length of the cables and the price of the chosen battery. For the first question of our case (where the batteries are stationary) this meant that we had to find  a way to connect every house to the nearest battery (which meant that the cable cost are the lowest possible). Exactly this was done by means of our lower bound algorithm. But obviously this solution does not suffice simply because the maximum capacity isn’t taken into account when connecting. So we ran in to one  and probably the main problem of our case namely the fact that the houses have different output and the batteries limited capacity, because this means that although you find the best way to connect houses to batteries. This doesn’t mean that in practice this is the best way. So because the theoretical best way to connect is not available you have no aim where to end, and because of the fact that the space state is so incredibly large it is quite impossible to actually guarantee that that we reached our goal.

We found “good” solutions to our problem by running a hill climber algorithm. But because we only had a limited amount of batteries, we could supply every house with a battery, but not in every way. And this is where capacity and different output again creates a problem, namely that when running the hill climber we couldn’t connect a house with an output too large for any battery, because the batteries are already full. So we had to swap houses between batteries to create space for that one house. This often had a negative effect on the total costs of a neighbourhood, because the swaps that are performed are random. We created a heuristics that made these swaps more efficient by making a priority list of nearest batteries wich the hillclimber runs down.

Eventually we could move the batteries. A big question was where to move the batteries? But eventually that question was quickly answered by our k means algorithm which moves the batteries so that the total distance from each house to a battery is reduced over every iteration. Again output and capacity are our greates enemy. This is because the spots we find might be optimal to reduce total distance, so in theory reduces total cable length, but it might be that a optimal spot for a battery is in the middle of a cluster of houses with high output, which means that all those houses will not fit in the nearest battery. 

The final problem includes different types of batteries. this means that in theory you want to find the best positions with the best configuration of batteries. But again the problem is that you can’t find this solution, because the configuration of batteries might not support the most efficient clusters because the houses do not have the same output, so the cable length are not minimal.

## Making statespace smaller
To reduce the statespace we adjusted the hillclimber. First, it selected random cables and swapped these. We implemented a function that first makes a priority list of the nearest batteries for each house. The longest cables are the ones which we cost the most, so these are the cables we want to swap. This way the "good" cables stay as they are and the hillclimber has a shorter runtime.

## Simmulated Annealing coolingschemes

| Neighborhood  | 0.0005     | 0.001      | 0.005  |
| ------------  | ---------- | ---------- |------  |
| 1 - Average   | €56642.2   | €57014.8   |€60706.6|    
|   - Minimum   | €56347     | €56644     |€59893  |
| 2 - Average   | €46860.1   | €47311.9   |€51143.2|
|   - Minimum   | €46222     | €46636     |€50533  |
| 3 - Average   | €44304.1   | €44706.4   |€48896.8|
|   - Minimum   | €43999     | €44341     |€47581  |



## Plots
- random distribution plot verbinden (bij lower+upperbound)
- random distribution plot huizen plaatsen (bij lower+upperbound)
- random connected + simulated annealing connected
![simann](https://user-images.githubusercontent.com/44001399/49603363-59f81100-f98b-11e8-815e-ef5e024c919e.png)

- random + k means
![random_connect](https://user-images.githubusercontent.com/44001399/49603454-a17e9d00-f98b-11e8-8a51-9298eacbeaa2.png)

