class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self, percentage):
        self.salary += self.salary * (percentage / 100)
        # return bonus
    
    def __str__(self) -> str:
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}"
    
employee = Employee(1, "John Doe", 50000);
employee2 = Employee(2, "Jane Smith", 60000);
print(employee.calculate_bonus(10))
print(employee)
# print(type(employee))
# print(empooyee)