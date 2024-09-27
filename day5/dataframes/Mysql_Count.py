import mysql.connector
from concurrent.futures import ThreadPoolExecutor
import threading

# Function to fetch data from MySQL
def fetch_data():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='cris_db'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Function to filter names and update the count
def filter_names(employees, count_lock, count_found):
    local_count = 0
    results = []
    for employee in employees:
        if employee['name'].startswith('R'):
            results.append(employee)
            with count_lock:
                count_found[0] += 1  # Update the shared count
                local_count += 1
    return results, local_count

# Main execution
if __name__ == "__main__":
    # Fetch data from the database
    employees = fetch_data()

    # Initialize shared resources
    count_lock = threading.Lock()
    count_found = [0]  # Use a list to allow sharing the variable

    # Use ThreadPoolExecutor to filter names concurrently
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Split the list of employees into chunks for each worker
        chunk_size = len(employees) // 4
        futures = [executor.submit(filter_names, employees[i:i + chunk_size], count_lock, count_found) 
                   for i in range(0, len(employees), chunk_size)]
        
        # Gather the results
        results = []
        for future in futures:
            filtered_results, local_count = future.result()
            print(f"Processed {local_count} records from worker {threading.current_thread().name}")
            results.extend(filtered_results)

    # Print filtered results and count
    print("Employees whose names start with 'R':")
    for result in results:
        print(result)

    print(f"Total records found: {count_found[0]}")
