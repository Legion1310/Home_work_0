"""Игра "Угадай число". Компьютер сам загадывает и сам угадывает число. Версия - 3"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # Количество попыток
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_number = np.random.randint(1, 101) # Переменная, которое генерирует случайное число
    number_one = 0 # Переменная для стартового отсчета

    if number != random_number: # Цикл для подбора числа,если сслучайное число не совпало с загаданным
        while number != number_one:
            count += 1
            if number > number_one:
                number_one += 10
            elif number < number_one:
                number_one -= 1
    else:
        count += 1
    return count
print(game_core_v3())