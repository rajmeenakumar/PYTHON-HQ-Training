from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import threading

def process_data(record):
    print("Processing record by thread:", threading.current_thread().name)
    record['ip_address'] = f"192.168.1.{record['id']}"
    return record

with open('MOCK_DATA.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    records = list(reader)
    # print(records)

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(process_data, record) for record in records]
    for future in as_completed(futures):
        try: 
            print(future.result())
        except ValueError as e:
            print(f"Task {e.args[0]} skipped")