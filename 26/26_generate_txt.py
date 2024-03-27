import random

n = random.randrange(2000, 10000)  # Кол-во нейросетей в файле
days_3 = []  # Кол-во дней обучения 3-го типа
nn_str = ""  # Здесь будем хранить записи каждой нейросети
for _ in range(n):
    days = random.randrange(1, 11)  # Выбираем кол-во дней для обучения
    type_n = random.randrange(1, 4)  # Выбираем тип нейросети

    # В зависимости от сложности нейросети умножаем время на коэффициент
    if type_n == 2:
        days *= random.randrange(2, 5)
    if type_n == 3:
        days *= random.randrange(4, 10)
        days_3.append(days)  # Если нейросеть 3-го типа, то добавляем ее в список со временем
    nn_str += f"{days} {type_n}\n"

nn_str = nn_str[:-1]  # Убираем последний перенос строки

# Считаем сколько нейросетей успеет обучить Никита
days_3.sort()
s = 0
count = 0
while s + days_3[count] <= 365:
    s += days_3[count]
    count += 1

win = random.randrange(0, 2)  # Выбираем выиграет или проиграет
if win:  # Если Никита выиграет то мы вычитаем из его результата рандомное число от 1 до 10
    andrey_count = count - random.randrange(1, 11)
    andrey_count = max(0, andrey_count)
else:  # Иначе прибавляем к кол-ву нейросетей Андрея число от 0 до 10
    andrey_count = count + random.randrange(0, 11)
    andrey_count = min(n, andrey_count)
print(win)
# Записываем входные данные в файл
full_str = f"{n} {andrey_count}\n{nn_str}"
with open("26_data.txt", "w") as file:
    file.write(full_str)
