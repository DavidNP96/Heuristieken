# Results

## Statespace, upperbound and lowerbound
### Stationary
#### Statespace
At first the batteries are stationary. The statespace in this situation is
5^150. This is because there are 5 batteries and per battery it has 150 houses
it can connect to, so this is the number of different connections that can be made.

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
When the batteries can be moved the statespace is (2500^5) * (5^150). There will still be 5^150 different possible connections, but the 5 batteries can be on 2500 different locations on the grid.

#### Lowerbound and upperbound
K-means and then lowerbound.

| Neighborhood | Upperbound | Lowerbound |
| ------------ | ---------- | ---------- |
| 1            | €103030    | €53188     |
| 2            | €96253     | €45268     |
| 3            | €101491    | €42757     |

### Different battery types
#### Statespace
In the last situation there will be 3 different battery types. The 3 different types of batteries can be on 2500 different positions on the grid, but not on the same position as another battery. Also, there can be as many batteries as you want. So all the grid point have the posibility to have a battery on it. There are 2500 grid points and 150 houses, so the 150 have 2500 possible points to connect to. These two components together give the following statespace: (3^2500!) * 2500^150.

#### Lowerbound and upperbound
VERANDEREN

| Neighborhood | Upperbound | Lowerbound |
| ------------ | ---------- | ---------- |
| 1            | €103030    | €53188     |
| 2            | €96253     | €45268     |
| 3            | €101491    | €42757     |

## What makes this case difficult?
- laatste huis kon niet verbonden worden
- upper- lowerbound bedenken voor punt c en d
- clusters kiezen k-means

## Zoekruimte verkleinen
Misschien huizen weggooien die al goed verbonden zijn. Aangeven wat er veranderd is.

## Plots
- random distribution plot verbinden (bij lower+upperbound)
- random distribution plot huizen plaatsen (bij lower+upperbound)
- random connected + simulated annealing connected
![simann](https://user-images.githubusercontent.com/44001399/49603363-59f81100-f98b-11e8-815e-ef5e024c919e.png)

- random + k means

