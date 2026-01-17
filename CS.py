# print(3 > 4)   # False
# print(3 < 4)   # True
# print(3 == 4)  # False
# print(4 == 4)  # True
# print(3 != 4)  # True
# print(3 >= 4)  # False
# print(3 <= 4)  # True


# age = 17

# if age >= 18:
#     print("You are an adult.")
# elif age < 18:
#     print("You are a minor.")
# else:
#     print("Invalid age.")


# Nested If-Else

citizen = True
age = 20

# if citizen:
#     if age >= 18:
#         print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# if citizen and age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# age = 19
# is_student = True

# if age < 18 and is_student:
#     print("You are eligible for a discount.")
# else:
#     print("You are not eligible for a discount.")

developer = 'Naomi'

result = developer.endswith('N')

print(result)

def greet():
    pass
    
print(greet())

example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # ?