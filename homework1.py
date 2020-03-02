"""Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """


def catalog_finder(url_list):
    result_list = []
    for i in range(len(url_list)):
        b = url_list[i].find('/catalog/')

        if b > 0:
            result_list.append(url_list[i])

    return result_list


url_list = ['http://www.fignya/catalog/ru', 'http://www.l2.ru',
     'https://github.com/yehorlevchenko/hillel_python_01/blob/master/01_data_types/tasks_01.py',
     'https://lms.ithillel.ua/groups/5dce5fab585879643f2c5b14/lessons/5e5010172758b447bb7f84ef',
     'https://www.github/catalog/.com']

print(catalog_finder(url_list))