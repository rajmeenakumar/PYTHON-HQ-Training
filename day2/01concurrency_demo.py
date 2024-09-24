import concurrent.futures
import threading

def task(n):
    print(threading.current_thread().name, "processing", n)
    return n * n

list = [1, 2, 3, 4, 5]

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # executor.map(task, list)
    for item in list:
        executor.submit(task, item)