"""
   Дописать функцию, которая будет принимать 2 строки и вставлять вторую
   в середину первой
   """

def mix_strings(str1, str2):
    a = str1[:len(str1) //2]
    b = str1[len(str1) // 2:]
    result_str = a + str2 + b

    return result_str

str1 = 'Hello World'
str2 = ' nice'

print(mix_strings(str1,str2))