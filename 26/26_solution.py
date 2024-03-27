with open("26_data.txt") as file:
    data = file.readlines()
    # Считываем кол-во нейросетей и результат Андрея
    n, andrey_count = [int(el) for el in data[0].split()]
    days_3 = []
    for i in range(1, n):
        # Считываем кол-во дней дня обучения и тип нейросети
        count_days, type_nn = [int(el) for el in data[i].split()]
        if type_nn != 3:  # идем дальше если тип не 3
            continue
        days_3.append(count_days)  # добавляем во времена 3й нейросети текущее время
    days_3.sort()

    s = 0  # Сумма дней
    count = 0  # Количество нейросетей
    # Если мы успеваем обучить еще одну нейросеть, то добавляем сумму и кол-во
    while s + days_3[count] <= 365:
        s += days_3[count]
        count += 1
    if count > andrey_count:  # Если получилось больше то мы выиграли в противном случае проиграли
        print("Yes")
    else:
        print("No")
