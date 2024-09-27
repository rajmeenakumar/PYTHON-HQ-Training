import mysql.connector
from concurrent.futures import ThreadPoolExecutor

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

# Function to filter names
def filter_names(employees):
    return [employee for employee in employees if employee['name'].startswith('R')]

# Main execution
if __name__ == "__main__":
    # Fetch data from the database
    employees = fetch_data()

    # Use ThreadPoolExecutor to filter names concurrently
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Split the list of employees into chunks for each worker
        chunk_size = len(employees) // 4
        futures = [executor.submit(filter_names, employees[i:i + chunk_size]) for i in range(0, len(employees), chunk_size)]
        
        # Gather the results
        results = []
        for future in futures:
            results.extend(future.result())

    # Print filtered results
    print("Employees whose names start with 'R':")
    for result in results:
        print(result)
