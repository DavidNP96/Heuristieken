# Neighborhood class containing grid and connect function
Class Neighborhood(Object):

  constant int grid_size = 50
  constant int total_houses = 50
  constant int total_batteries = 5

  int Connect(house, battery):
    x_distance = abs(house.x_location - battery.x_location)
    y_distance = abs(house.y_location - battery.y_location)

    
