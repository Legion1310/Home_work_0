"""Игра угадай число"""

import numpy as np # Импорт библиотеки NunPy

np.random.seed(1)  # Фиксируем сид для воспроизводимости
number = np.random.randint(1, 101) # Загадываем число
count = 0 # Счетчик количества попыток

while True: # Открываем бесконечный цыкл
    count += 1 # Включаем счетчик
    predict_number = int(input("Угадай число от 1 до 100: ")) # Переменная числа, которое вводит пользователь
    # Условие подбора результата
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # Конец игры выход из цикла