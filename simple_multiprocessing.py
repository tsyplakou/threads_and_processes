import os
from multiprocessing import Process, current_process
import time

# Функция для вычисления квадрата числа
def calculate_square(number):
    time.sleep(5-number)
    process_name = current_process().name  # Имя текущего процесса
    print(f"Процесс {process_name} (PID {os.getpid()}): вычисляю квадрат {number}")
    result = number * number
    print(f"Процесс {process_name}: результат {number}^2 = {result}")


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]  # Числа для вычисления квадратов

    # Создаём список процессов
    processes = []

    for number in numbers:
        # Создаём процесс для вычисления квадрата каждого числа
        process = Process(target=calculate_square, args=(number,))
        processes.append(process)  # Добавляем процесс в список
        process.start()  # Запускаем процесс

    # Ожидаем завершения всех процессов
    for process in processes:
        process.join()

    print("Все процессы завершены")
