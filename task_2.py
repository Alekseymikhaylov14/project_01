# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!
city = ['Москва', 'Брянск', 'Рязань']
# Создайте список списков населения перечисленных городов
people = [[13010112], [379152], [528599]]
# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек
print('Население Брянска -', people[1], 'человек')
# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек
for people1 in people[0]:
    for people2 in people[1]:
        for people3 in people[2]:
            print('Итого размер населения', people1 + people2 + people3, 'человек')
