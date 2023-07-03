# Date of Last Practice:

# Create a list
my_list = [1, 2, 3, 4, 5]

# Access elements in a list
print(f"my_list[0] = {my_list[0]}")
print(f"my_list[-1] = {my_list[-1]}")

# Modify elements in a list
my_list[0] = 6
print(f"my_list[0] = {my_list[0]}")

# Add elements to a list
my_list.append(8)
print(f"my_list = {my_list}")

# Remove elements from a list
my_list.remove(8)
print(f"my_list = {my_list}")

# Iterate over a list
for index, item in enumerate(my_list):
    print(f"my_list's item[{index}] = {item}")

# List comprehension
#
# Syntax: new_list = [expression for item in iterable if condition]
# The reason the following code doesn't work as intended is because
# the append() method expects a single element to be added to the list,
# not a generator expression.
#
# odd_numbers = []
# odd_numbers.append(item for item in my_list if item % 2 == 1)
# print(f"odd_numbers = {odd_numbers}")
squared_list = [item**2 for item in my_list]
print(f"squared_list = {squared_list}")

# List comprehension with if condition
even_numbers = [item for item in my_list if item % 2 == 0 and len(my_list) == 5]
print(f"even_numbers = {even_numbers}")

# Sort a list
sorted_list = my_list.sort()
sorted_list_in_reverse = my_list.sort(reverse=True)

# Chech if an element exists in a list
if 3 in my_list:
    print(f"The value 3 is in the list")

# Search for an element's index in a list
index = my_list.index(3)
print(f"The value 3 is in index {index}")

# Combine two lists
list_1 = [1, 2, 3]
list_2 = ["A", "B", "C"]
combined_list = list_1 + list_2
print(combined_list)

# Create a 2-D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access and update a 2-D matrix
print(f"matrix[0][1] = {matrix[0][1]}")
matrix[0][1] = 10
print(f"matrix[0][1] = {matrix[0][1]}")

# Delete elements from a 2-D matrix
del matrix[0][1]
print(f"matrix[0][1] = {matrix[0][1]}")
print(f"matrix = {matrix}")
