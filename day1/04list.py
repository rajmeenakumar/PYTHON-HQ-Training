even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9, 9]

# Concatenate the lists

combined_list = even_numbers + odd_numbers
print(combined_list)

combined_list.reverse();
print(combined_list)

# Sort the list in ascending order

combined_list.sort();
print(combined_list)

# Remove duplicates from the list

combined_list = list(set(combined_list))
print(combined_list)

print(max(combined_list))