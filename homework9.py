"""
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """

def even_int_generator(x):
    from random import randint
    lst = [randint(0, 100) for i in range(x)]
    even_int_list = []
    for i in range(len(lst)):
        b = (randint(0, 100))
        if lst[i] % 2 != 1:
            even_int_list.append(lst[i])


    print(even_int_list)
    return even_int_list

even_int_generator(25)
