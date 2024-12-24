import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)


def print_letters():
    for letter in 'abcde':
        time.sleep(1.5)
        print(letter)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
print("Поток 1 завершен")

thread2.join()
print("Поток 2 завершен")

print("Оба потока завершены")
