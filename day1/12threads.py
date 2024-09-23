import threading

def print_hello(name):
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

print("Thread name" + threading.currentThread().getName());