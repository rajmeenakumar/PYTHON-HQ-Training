
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


def task(n):
    if n == 7:
        raise ValueError("Task 7 is skipped")
    time.sleep(2)
    print(threading.current_thread().name, "processing", n)
    return n * n

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in as_completed(futures):
        try: 
            print(future.result())
        except ValueError as e:
            print(f"Task {e.args[0]} skipped")