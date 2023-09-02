# Date of Last Practice:

# In Python, the set() data structure is a built-in collection type that
# represents an unordered collection of unique elements.
# It is implemented using a hash table, which provides efficient insertion, deletion, and
# membership testing operations. The average time complexity of num in my_set is O(1),
# making it faster compared to iterating over a list or checking for membership in a dictionary.


# Removing duplicates from a list: Sets are often used to eliminate duplicate elements
# from a list by converting the list to a set and then converting it back to a list.
# Since sets only store unique elements, any duplicates are automatically removed. For example:
my_list = [1, 1, 2, 4, 6, 2, 7, 8]
unique_elements = list(set(my_list))
print("Unique elements:", unique_elements)


# Checking for membership: Sets are useful for quickly checking if an element exists
# in a collection without iterating over the entire collection.
# This is particularly efficient for large collections. For example:
my_set = {1, 2, 3, 4, 5}
print("Is 2 in my_set?", 2 in my_set)
print("Is 6 in my_set?", 6 in my_set)


# Set operations: Sets support various set operations such as union, intersection, difference,
# and symmetric difference. These operations can be handy for tasks like finding common elements
# between sets, finding unique elements, or comparing sets. For example:
set_1 = {1, 2, 3}
set_2 = {3, 4, 5, 6}
print("Union:", set_1.union(set_2))
print("Intersection:", set_1.intersection(set_2))
print("Difference:", set_1.difference(set_2))
print("Symmetric Difference:", set_1.symmetric_difference(set_2))
