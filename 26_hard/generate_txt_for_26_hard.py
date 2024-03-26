"""Скрипт, который генерирует данные для задачи"""
import random

data = ""  # Здесь храним строку, которую будем сохранять в файл
regions_sums = []  # Здесь храним баллы команд которые мы уже сгенерировали
for _ in range(89):
    n = random.randrange(3, 20)  # Выбираем кол-во участников
    balls = [random.randrange(0, 101) for _ in range(n)]  # Выбираем их баллы

    # Смотрим какой балл получился
    sorted_balls = sorted(balls)
    team_ball = sorted_balls[-1] + sorted_balls[-2] + sorted_balls[-3]

    # Повторяем все то же самое если команда с таким баллом уже есть
    while team_ball in regions_sums:
        n = random.randrange(3, 20)  # Выбираем кол-во участников
        balls = [random.randrange(0, 101) for _ in range(n)]  # Выбираем их баллы

        # Смотрим какой балл получился
        sorted_balls = sorted(balls)
        team_ball = sorted_balls[-1] + sorted_balls[-2] + sorted_balls[-3]

    regions_sums.append(team_ball)  # Добавляем балл региона к списку баллов всех регионов
    data += f"{n}\n{' '.join(str(el) for el in balls)}\n"  # формируем строку команды

data = data[:-1]  # Удаляем последний перенос строки

with open("26_hard/26_data.txt", "w") as file:  # записываем нашу строку в файл и сохраняем его
    file.write(data)
