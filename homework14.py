"""
  Дан массив чисел.
  [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
  вывести исходный массив в обратном порядке
  """


def reversed_list(input_list):
    reverse = []
    for i in range(len(input_list)):
        reverse.append(input_list[-1-i])
    print(reverse)
    return reverse

a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


reversed_list(a)

