from multiprocessing import Process, Queue, cpu_count
import os


def file_reader_sequence(file_path):
    total_words = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            total_words += len(line.split())
    return total_words


# Функция для чтения файла и передачи строк в очередь
def file_reader(file_path, line_queue):
    print("Чтение файла...")
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_queue.put(line)  # Отправляем строку в очередь
    line_queue.put(None)  # Сигнал завершения
    print("Чтение завершено.")


# Функция для подсчёта слов в строках
def word_counter(line_queue, result_queue):
    while True:
        line = line_queue.get()
        if line is None:  # Проверяем сигнал завершения
            line_queue.put(None)  # Передаём сигнал другим процессам
            break
        word_count = len(line.split())
        result_queue.put(word_count)  # Отправляем результат


# Функция для сбора результатов
def result_collector(result_queue):
    total_words = 0
    while True:
        count = result_queue.get()
        if count is None:  # Проверяем сигнал завершения
            break
        total_words += count
    print(f"Общее количество слов: {total_words}")


# Главный процесс
if __name__ == "__main__":
    import time

    start_time = time.time()

    # Пусть файл будет большой текстовый файл
    file_path = "book-war-and-peace.txt"

    # Проверяем наличие файла
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     f.write("Python multiprocessing example asd. " * 1000 + "\n" * 100)  # Генерация тестового файла

    # Создаём очереди для передачи данных
    line_queue = Queue()
    result_queue = Queue()

    # Создаём процессы
    reader_process = Process(target=file_reader, args=(file_path, line_queue))
    workers = [Process(target=word_counter, args=(line_queue, result_queue)) for _ in range(cpu_count() - 2)]
    result_process = Process(target=result_collector, args=(result_queue,))

    # Запускаем процессы
    reader_process.start()
    for worker in workers:
        worker.start()
    result_process.start()

    # Ожидаем завершения процессов
    reader_process.join()
    for worker in workers:
        worker.join()

    result_queue.put(None)  # Сигнал завершения для сборщика
    result_process.join()

    print("Подсчёт завершён.")

    print(f"Время выполнения: {time.time() - start_time:.2f} секунд")


    start_time = time.time()

    print(file_reader_sequence(file_path))  # Проверка результата с использованием последовательного чтения

    print(f"Время выполнения последовательного чтения: {time.time() - start_time:.2f} секунд")
