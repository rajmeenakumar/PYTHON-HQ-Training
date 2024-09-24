import threading

shared_couter = 0

def increment_counter():
    global shared_couter;
    for _ in range(10000):
        shared_couter +=1

for _ in range(500000):
    threading.Thread(target=increment_counter).start()

print(f'Final value {shared_couter}')