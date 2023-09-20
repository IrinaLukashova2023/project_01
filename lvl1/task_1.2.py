# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

from random import sample

rand_song = sample(my_favorite_songs, 3)
print ( '\n' "Пункт A, cлучайный выбор песен:",
        '\n', rand_song [0],
        '\n', rand_song [1],
        '\n', rand_song [2]
     )

import datetime

total_time = datetime.timedelta()
time_songs = [
    str(rand_song[0][1]),
    str(rand_song[1][1]),
    str(rand_song[2][1])
]

for time in time_songs:
    minutes, seconds = time.split(".")
    minutes, seconds = int(minutes), int(seconds)
    total_time += datetime.timedelta(minutes=minutes, seconds=seconds)

sec = total_time.total_seconds()
print("Три песни звучат – ",
      '\n', total_time, "минут",
      )

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
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
rsong = list(my_favorite_songs_dict.items())
song_choice = sample(rsong, 3)
print ( '\n', "Пункт В, случайный выбор песен:",
        '\n', song_choice[0],
        '\n', song_choice[1],
        '\n', song_choice[2]
     )

import datetime

total_time2 = datetime.timedelta()
time_songs2 = [
    str(song_choice[0][1]),
    str(song_choice[1][1]),
    str(song_choice[2][1])
]

for time in time_songs2:
    minutes, seconds = time.split(".")
    minutes, seconds = int(minutes), int(seconds)
    total_time2 += datetime.timedelta(minutes=minutes, seconds=seconds)
sec1 = total_time2.total_seconds()

print("Три песни звучат – ",
      '\n', total_time2, "минут",
      )
