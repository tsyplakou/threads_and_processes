import threading
import time

import psycopg2


def execute_query(query):
    conn = psycopg2.connect(
        dbname='book_room',
        user='postgres',
        password='postgres',
        host='localhost',
        port=5432,
        keepalives=1,
        keepalives_idle=30,
        keepalives_interval=10,
        keepalives_count=5,
    )
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(f"Выполнен запрос: {query}")

queries = [
    "select * from location_location",
    "select * from location_location",
    "select * from location_location",
    "select * from room_booking_booking",
    "select * from room_room",
]

threads = []

start_time = time.time()
for query in queries:
    thread = threading.Thread(target=execute_query, args=(query,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Все запросы завершены. Общее время: {time.time() - start_time:.2f} секунд")


start = time.time()

for query in queries:
    execute_query(query)

print(f"Все последовательные запросы завершены. Общее время: {time.time() - start:.2f}")
