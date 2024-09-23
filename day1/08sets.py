a = set(["John", "Doe", "Jane", "Doe"])
print(a)

# Adding a new element

a.add("Jane")
print(a)

# Removing an element

a.remove("Doe")
print(a)

# Checking if an element exists

print("John" in a)  # True
print("Jane" in a)  # True

# union of two sets

b = set(["Alice", "Bob", "Charlie", "Alice"])
print(a.union(b))

# intersection of two sets

print(a.intersection(b))