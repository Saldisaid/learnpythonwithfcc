# def outer_func():
#     msg = 'Hello'

#     def inner_func():
#         msg = 'Hi'
#         return msg

#     inner_func()
#     return msg

# print(outer_func())

my_list = [3.99, '42', True]
my_new_list = [int(i) for i in my_list]
print(my_new_list)

developer = 'Jessica'
result = list(developer)
print(result)

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
i = programming_languages.index('Python', 3)
print(i)