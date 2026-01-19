# lang = ('Python', 'Java', 'C++', 'JavaScript')
# # lang[0] = 'Go'  # This will raise a TypeError
# # print(lang)

# name = 'Saldi'
# print(tuple(name))

# methohds in tuple
lang = ('Python', 'Java', 'C++', 'JavaScript', 'Python')
# print(lang.count('Python'))  # Output: 2
# print(lang.index('Java'))  # Output: 1
# print(lang.index('Python', 1))

# print(sorted(lang))  # Output: ['C++', 'Java', 'JavaScript', 'Python', 'Python']
# print(sorted(lang, key=len))  # Output: ['C++', 'Java', 'Python', 'Python', 'JavaScript']
print(sorted(lang, reverse=True))  # Output: ['Python', 'Python', 'JavaScript', 'Java', 'C++']

