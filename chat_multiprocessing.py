import time
from multiprocessing import Process, Pipe


def chat_member(conn, messages):
    for message in messages:
        conn.send(message.encode())
        time.sleep(0.001)


def receiver(conn):
    while True:
        message = conn.recv().decode()
        if not message:
            break
        print(f"{time.time()}: {message}")


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    processes = []

    processes.append(Process(target=chat_member, args=(parent_conn, ["Привет", "Как дела?", "Хорошо"])))
    processes.append(Process(target=chat_member, args=(parent_conn, ["Привет!", "Норм. Как твои?", "Здорово!"])))
    processes.append(Process(target=receiver, args=(child_conn,)))

    for process in processes:
        print(time.time())
        process.start()

    for process in processes:
        process.join()
