# contains helper functions such as sort algorithms

def selection_sort(input_list):
    """
    Sorts houses based on max_output.
    """

    i = 0

    for i in range(len(input_list)):
        house_1 = input_list[i]
        new_pos = i
        for j in range( idx +1, len(input_list)):
            house_2 = input_list[j]
            if house_1.output > input_list[j]:
                new_pos = j
        i += 1
        # Swap the minimum value with the compared value
        input_list[i], input_list[new_pos] = input_list[new_pos], input_list[i]

    return input_list
