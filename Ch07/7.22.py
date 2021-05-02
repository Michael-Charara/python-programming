def sum_neighbors(list):
    new_list = []
    new_list.append(list[0] + list[1])
    x = 1
    while x < len(list) - 1:
        new_list.append(list[x - 1] + list[x] + list[x + 1])
        x += 1
    new_list.append(list[x - 1] + list[x])

    return new_list
