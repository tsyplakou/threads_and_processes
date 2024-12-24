import threading
import time

import requests

# Список URL для запросов
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]

# Функция для выполнения запроса
def fetch_url(url):
    print(f"Начинаю загрузку: {url}")
    try:
        response = requests.get(url)
        print(f"Загружено {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")

# Создаём список потоков
threads = []

start_time = time.time()

# Создаём потоки для каждого URL
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

# Ждём завершения всех потоков
for thread in threads:
    thread.join()

end_time = time.time()

print(f"Все запросы завершены. Общее время: {end_time - start_time:.2f} секунд")

start = time.time()
print("Sequence calls")

for url in urls:
    fetch_url(url)

print(f"Все последовательные запросы завершены. Общее время: {time.time() - start:.2f}")
