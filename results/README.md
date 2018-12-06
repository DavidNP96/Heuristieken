# Results

### Statespace
#### Stationary  
At first the batteries are stationary. The statespace in this situation is
5^150. This is because there are 5 batteries and per battery it has 150 houses
it can connect to, so this is the number of different connections that can be made.

#### Moving  
When the batteries can be moved the statespace is (2500^5) * (5^150).

#### Different battery types  
In the last situation there will be 3 different battery types. This makes the
statespace three times bigger, so it will be (2500^5) * (5^150) * 3.

### Lowerbound and upperbound
The lowerbound is the hypothetical situation where the costs of the neighborhood are the lowest possible.
All houses are connected to the closest battery. The upperbound is the opposite situation, so where all houses
are connected to the furthest battery. However, these situation will not be possible, because the capacity of 
the batteries will not be taken into account.

| Neighborhood | Upperbound | Lowerbound |
| ------------ | ---------- | ---------- |
| 1            | €103030    | €53188     |
| 2            | €96253     | €45268     |
| 3            | €101491    | €42757     |
