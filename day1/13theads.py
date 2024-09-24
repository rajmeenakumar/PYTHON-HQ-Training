import threading
import time


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self, percentage):
        time.sleep(2);
        self.salary += self.salary * (percentage / 100)
        # return bonus
    
    def __str__(self) -> str:
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}"
    
employee = Employee(1, "John Doe", 50000);
employee2 = Employee(2, "Jane Smith", 60000);
employee3 = Employee(3, "Alice Johnson", 70000);
employee4 = Employee(4, "Bob Brown", 80000);
employee5 = Employee(5, "Charlie Davis", 90000);

employees = [employee, employee2, employee3, employee4, employee5]

#print start time

start_time = time.time()

threads = []
for employee in employees:
    t= threading.Thread(target=employee.calculate_bonus, args=(10,))
    t.start()
    threads.append(t)
    # employee.calculate_bonus(10)


for t in threads:
    t.join()
# print end time

end_time = time.time()

print(f"Total time taken: {end_time - start_time} seconds")

# print(employee.calculate_bonus(10))

# print(type(employee))
# print(empooyee)