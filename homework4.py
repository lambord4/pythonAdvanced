"""
   Дописать функцию, которая считает сколько раз каждая из букв
   встречается в строке, разложить буквы в словарь парами
   {буква:количество упоминаний в строке}
   """

a = 'Дописать функцию, которая считает сколько раз каждая из букв ' \
    'встречается в строке, разложить буквы в словарь парами ' \
    '{буква:количество упоминаний в строке}'


for i in range(len(a)):
    dict = {}
    dict[a[i]] = a.count(a[i])
    print(dict)