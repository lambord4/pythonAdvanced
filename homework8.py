"""
   Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
   keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
   """


def square_dict(lst):
    dict1 = {}
    for i in range(len(lst)):
        dict1[lst[i]] = lst[i]*lst[i]

    return dict1


keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square_dict(keys))
