"""
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """

def get_str_center(input_str):
    output_str = ''
    if len(input_str) % 2:
        output_str += input_str[len(input_str) // 2 - 1] + input_str[len(input_str) // 2] + input_str[len(input_str) // 2 + 1]
    else:
        output_str += input_str[len(input_str) // 2 - 1] + input_str[len(input_str) // 2]

    print(output_str)
    return output_str

x = input('Введите текст:')
get_str_center(x)
