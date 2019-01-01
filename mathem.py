import random
import numexpr as ne
from datetime import datetime


def valid_answer(user_answer):
    try:
        return int(user_answer)
    except (TypeError, ValueError):
        return int(valid_answer(input('Введи повторно ответ: ')))


class RunMathem(object):
    def __init__(self):
        pass

    def start_task(self, number_of_jobs=40):
        self.number_of_jobs = number_of_jobs


        task = 1
        truly = 0
        not_truly = 0
        i = 0

        while i < self.number_of_jobs:


            print('########## Задание №' + str(self.task) + ' ##########')
            print(expr)
            if valid_answer(input('Введи ответ: ')) == answer:
                # print('Правильный ответ')
                self.truly += 1
            else:
                # print('Не верно')
                self.not_truly += 1
            task += 1
            i += 1

        # Время за которое решено задание
        time_for_decision = str(datetime.now() - time_now).split('.')[0]

        return


    def get_number(self, max_number):
        self.max_number = max_number
        return random.randint(1, self.max_number)

    def valid(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

        operators = '+', '-'
        action = random.choice(operators)
        expr = self.first_number + ' ' + action + ' ' + self.second_number
        answer = ne.evaluate(expr).item()

        if answer < 0:
            continue
        elif answer > self.max_number:
            continue
        else:
            return answer

    def print_answer(self):
        # Вывести отчёт
        print('\n########## Итог задания ##########')
        print('Правильных ответов: ', truly)
        print('Неверных ответов: ', not_truly)
        print('Время потраченое на решение: ', time_for_decision)

        if not_truly == 0:
            example_error = 0
        elif 1 <= not_truly < 4:
            example_error = 1
        elif 4 <= not_truly < 7:
            example_error = 2
        else:
            example_error = 3

        if time_for_decision <= '0:02:00':
            time_error = 0
        elif '0:02:00' < time_for_decision <= '0:03:00':
            time_error = 1
        elif '0:03:00' < time_for_decision <= '0:04:00':
            time_error = 2
        else:
            time_error = 3

        all_error = example_error + time_error

        # Оценка "5"
        if all_error == 0:
            print('"5" Ты супер-молодец! Так держать!')
            appreciation = 5
        # Оценка "4"
        elif all_error == 1 or (example_error == 1 and time_error == 1):
            print('"4" Молодец! Ты можешь и лучше!')
            appreciation = 4
        # Оценка "3"
        elif all_error == 3 or (all_error == 2 and (example_error == 2 or time_error == 2)):
            print('"3" Старайся лучше')
            appreciation = 3
        # Очень плохо
        else:
            print('"2" Нужно ещё подтянуть')
            appreciation = 2
