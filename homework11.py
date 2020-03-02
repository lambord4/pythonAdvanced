"""
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """

a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def filter_unique_int(input_list):
    unique_int_list = list(set(a))
    unique_int_list.sort()
    print(unique_int_list)


    return unique_int_list


filter_unique_int(a)


def filter_unique_int2(input_list2):
    unique_int_list2 = []
    for i in input_list2:
        if i not in unique_int_list2:
            unique_int_list2.append(i)
    unique_int_list2.sort()
    return unique_int_list2


print(filter_unique_int2(a))