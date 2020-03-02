"""
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """


def idiotic_str(input_str):
    a = ''
    for i in range(len(input_str)):
        if i % 2:
            a += input_str[i].upper()
        else:
            a += input_str[i].lower()
    print(a)
    return idiotic_str


x = input('Введите строку:')
print(idiotic_str(x))



