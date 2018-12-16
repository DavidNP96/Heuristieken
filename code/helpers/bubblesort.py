

def bubblesort(list, id_list):

    houses = id_list
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp_house_id = houses[j]
                temp_value = list[j]

                houses[j] = houses[j + 1]
                list[j] = list[j + 1]

                houses[j + 1] = temp_house_id
                list[j + 1] = temp_value
    return list, id_list

def bubblesort_rev(list, id_list):

    houses = id_list
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] < list[j + 1]:
                temp_house_id = houses[j]
                temp_value = list[j]

                houses[j] = houses[j + 1]
                list[j] = list[j + 1]

                houses[j + 1] = temp_house_id
                list[j + 1] = temp_value
    return list, id_list
