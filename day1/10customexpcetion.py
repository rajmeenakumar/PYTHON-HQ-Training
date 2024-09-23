class AgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return super().__str__()
    
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age < 18:
        raise AgeError("Age must be at least 18")
    
    return age

try:
    validate_age(17)
    print("Age is valid")
except AgeError as e:
    validate_age(24)
    print(e)

