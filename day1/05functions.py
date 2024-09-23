# lamda function
greet = lambda name: f"Hello, {name}!"

# Test the lambda function

print(greet("Alice"))  # Expected output: Hello, Alice!
print(greet("Bob"))   # Expected output: Hello, Bob!

# functions with variable number of arguments

def add_numbers(x, y, *args, a):
    return sum(args)

def multiply_numbers(*args):
    result = 1

#functions with keyword arguments

def greet_with_age(name, age):
    return f"Hello, {name}! You are {age} years old."