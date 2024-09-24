import csv
import threading

def process_data(record):
    print("Processing record:", record + "by thread:", threading.current_thread().name)
    record['ip_address'] = f"192.168.1.{record['id']}"
    return record

with open('MOCK_DATA.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    records = list(reader)
    print(records)