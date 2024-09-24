import concurrent.futures
import threading
import time

def task(n):
    time.sleep(2)
    print(threading.current_thread().name, "processing", n)
    return n * n

list = [1, 2, 3, 4, 5]

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = executor.map(task, list)
    for item in list:
        future = executor.submit(task, item)
        result = future.result();
        print(result)


    
       