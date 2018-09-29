#!/usr/bin/python3
# -*- coding: utf-8

import numexpr as ne
import random
from datetime import datetime
import pymysql


def get_connection_sql():
    try:
        db = pymysql.connect(host="192.168.12.153",
                             user="math",
                             passwd="NPISmPVI5I9C",
                             charset="utf8",
                             connect_timeout=1)
        return db
    except pymysql.Error as e:
        send_error_email(e)
        exit()


def insert_data_sql(times_now, mark, decision_time, correct, not_correct):
    db = get_connection_sql()
    try:
        cursor = db.cursor()

        sql = """INSERT INTO `lessons`.`mathematics`
                    (`datetime`, appreciation, decision_time, correct_answer, wrong_answers)
                    VALUES("%s", "%s", "%s", "%s", "%s");
        """ % (times_now, mark, decision_time, correct, not_correct)

        # print(sql)

        cursor.execute(sql)
        db.commit()
    except Exception as e:
        send_error_email(e)
        # print(e)
        exit()
    finally:
        # Закрываем коннект к базе
        db.close()


def send_error_email(e):
    # Отправка почты
    # from smtplib import SMTP_SSL
    from email.mime.text import MIMEText
    import smtplib

    # Данные для подключения
    fromaddr = '******'
    password = '******'

    # формирование сообщения
    msg = MIMEText(str(e), "", "utf-8")
    msg['From'] = fromaddr
    msg['To'] = fromaddr
    msg['Subject'] = "Ошибка в отчёте"

    # отправка
    # smtp = SMTP_SSL()
    smtp = smtplib.SMTP('******:587')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(fromaddr, password)
    smtp.sendmail(fromaddr, fromaddr, msg.as_string())
    smtp.quit()


def valid_answer(user_answer):
    try:
        return int(user_answer)
    except (TypeError, ValueError):
        return int(valid_answer(input('Введи повторно ответ: ')))


operators = '+', '-'

task = 1
truly = 0
not_truly = 0
i = 0
# Засекаем время
time_now = datetime.now()

while i < 40:
    first = str(random.randint(1, 10))
    two = str(random.randint(1, 10))
    action = random.choice(operators)
    expr = first + ' ' + action + ' ' + two
    answer = ne.evaluate(expr).item()
    # Если ответ менее '0' или более '10' запускаем новое задание
    if answer < 0:
        continue
    elif answer > 10:
        continue

    print('########## Задание №' + str(task) + ' ##########')
    print(expr)
    if valid_answer(input('Введи ответ: ')) == answer:
        # print('Правильный ответ')
        truly += 1
    else:
        # print('Не верно')
        not_truly += 1
    task += 1
    i += 1

# Время за которое решено задание
time_for_decision = str(datetime.now() - time_now).split('.')[0]

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

# Пишем в базу
insert_data_sql(str(time_now).split('.')[0], appreciation, time_for_decision, truly, not_truly)
