from random import randint

# До скольки таблица умножения?
table_number = int(input('До какого числа таблица?'))

# Сколько примеров?
number_of_examples = int(input('Сколько примеров?'))


def valid_answer(user_answer):
    try:
        return int(user_answer)
    except (TypeError, ValueError):
        return int(valid_answer(input('Введи повторно ответ: ')))


def create_answer(first, second):
    return first * second, str(first) + ' * ' + str(second)


truly = 0
not_truly = 0

# Вывести пример и ждать ответ
while number_of_examples:
    first_number = randint(1, table_number)
    second_number = randint(1, 10)
    answer, expr = create_answer(first_number, second_number)
    print(expr)
    if valid_answer(input('Введи ответ: ')) == answer:
        # print('Правильный ответ')
        truly += 1
    else:
        # print('Не верно')
        not_truly += 1
    number_of_examples -= 1

# Итог
print(f'Правильных ответов: {truly}\n', f'Не правильных ответов: {not_truly}')
