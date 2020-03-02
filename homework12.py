"""
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """

a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def three_biggest_int(input_list):
    b = list(set(input_list))
    b.sort()
    biggest_ints = (b[-1], b[-2], b[-3])
    print(biggest_ints)
    return biggest_ints

three_biggest_int(a)