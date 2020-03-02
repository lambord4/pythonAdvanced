"""
Заменить в произвольной строке согласные буквы на гласные.
"""


def replace_vowels(a):
    b = 'бвгджзйклмнпрстфхцчшщ'

    for i in range(len(a)):
        if a[i] in b:
            a = a.replace(a[i], 'а')
    print(a)
    return a


d = 'Заменить в произвольной строке согласные буквы на гласные.'
replace_vowels(d)
