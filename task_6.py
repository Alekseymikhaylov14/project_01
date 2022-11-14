# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
from random import sample
my_favorite_songs_1 = []
for time in my_favorite_songs.values():
    my_favorite_songs_1.append(time)
random = sample(my_favorite_songs_1, 3)
r1, r2, r3 = random[0], random[1], random[2]
print('Три песни звучат', int(r1 + r2 + r3), 'минут')
