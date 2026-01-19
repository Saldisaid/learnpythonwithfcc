lang = ['Python', 'Java', 'C++', 'JavaScript', 'Go']

# print(list(enumerate(lang)))  # Output: [(0, 'Python'), (1, 'Java'), (2, 'C++'), (3, 'JavaScript'), (4, 'Go')]
for i , lan in enumerate(lang, start=1):
    print(f"{i}. {lan}")

names = ['Saldi', 'Rina', 'Via']
age = [25, 24, 23]

# print(list(zip(names, age)))
for name, age in zip(names, age):
    print(f"{name} is {age} years old.")