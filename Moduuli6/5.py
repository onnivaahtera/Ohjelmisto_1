def sum_of_list(list):
    new_list = []
    for num in list:
        if num % 2 != 0:
            new_list.append(num)
    return new_list


list = [2, 5, 7, 1, 10, 3, 9, 6]
print(sum_of_list(list))
