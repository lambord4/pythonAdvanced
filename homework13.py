"""
   Дан массив чисел.
   [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
   вывести индекс минимального элемента массива
   """


def lowest_int_index(input_list):
    lowest_index = ()
    for i in range(len(input_list)):
        if input_list[i] == min(input_list):
            lowest_index = i
    print(lowest_index)
    return lowest_index


a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
lowest_int_index(a)
