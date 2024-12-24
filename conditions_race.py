import threading
import time

counter = 0
lock = threading.Lock()  # Блокировка для синхронизации доступа к counter

def increment():
    global counter
    for _ in range(100000):
        # 999 - 1
        # sleep
        # 999 - 2
        # sleep
        # 999+1 -> 1000 - 1
        # 999+1 -> 1000 - 2
        with lock:  # Блокируем доступ к counter
            temp = counter  # Читаем значение
            time.sleep(0.00001)  # Задержка для эмуляции длительной операции
            counter = temp + 1  # Пишем новое значение

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Итоговое значение counter: {counter}")
