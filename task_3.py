# Задача 3
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)
if 1 <= month <= 12:
    if month == 2:
        print(28) 
    elif 1 <= month <= 7 and month % 2 != 0 or 8 <= month <= 12 and month % 2 == 0:
        print(31)
    else:
        print(30)
else:
    print('Некорректно введен номер месяца') 
    