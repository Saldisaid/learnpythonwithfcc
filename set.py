my_sets = {1, 2, 3}
sets = { 7, 4, 5 }

# my_sets.add(4)
# print(my_sets)  # Output: {1, 2, 3, 4}
# my_sets.remove(4)
# print(my_sets)  # Output: {1, 2, 3}
# my_sets.discard(4)
# print(my_sets)  # Output: {1, 2, 3}
# my_sets.clear()
# print(my_sets)  # Output: set()

print(my_sets.issubset(sets))  # Output: False
print(sets.issuperset(my_sets))  # Output: False

print(my_sets.isdisjoint(sets))  # Output: True

union_set = my_sets | sets
print(union_set)  # Output: {1, 2, 3, 4, 5, 7}

intersection_set = my_sets & sets
print(intersection_set)  # Output: set()

difference_set = my_sets - sets
print(difference_set)  # Output: {1, 2, 3}

symmetric_difference_set = my_sets ^ sets
print(symmetric_difference_set)  # Output: {1, 2, 3,