import time
import threading

def print_hello(name):
    time.sleep(5)  # Simulating delay
    print(f"Hello, {name}!" + threading.currentThread().getName()) 

threads = []
for i in range(5):
    t = threading.Thread(target=print_hello, args=(i,))
    t.start();
    threads.append(t);
    # t.join();

for t in threads:
    t.join();
# t.join();

# print("Thread name" + threading.);
# print current thread name

print("Main thread name:", threading.currentThread().getName())