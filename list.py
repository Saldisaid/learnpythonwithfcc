# dev = 'Saldi said'
# list = list(dev)

# print(list)  # Output: ['S', 'a', '

# program_lang = ['Python', 'Java', 'C++', 'JavaScript']
# program_lang[0] =  'Go'
# print('rust' in program_lang)  # Output: False
# print('Go' in program_lang)    # Output: True
# del program_lang[1]
# print(program_lang)  # Output: ['Go', 'Java', 'C++', 'JavaScript']

# # Nested Lists
# dev = ['Saldi', 25, ['Python', 'JavaScript', 'C++']]
# print(dev[2])
# print(dev[2][0])

# name, age, lang = dev

# print(name)  # Output: Saldi
# print(age)   # Output: 25
# print(lang)  # Output: ['Python', 'JavaScript', 'C++']

# name, *rest = dev

# print(name)  # Output: Saldi
# print(rest)  # Output: [25, ['Python', 'JavaScript', 'C++']]s

# desert = ['cake', 'ice cream', 'pie', 'pudding', 'brownie']
# print(desert[1:4])

# numers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numers[::2])
# print(numers[::-1])

""" List Methods """
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [6, 7, 8, 9, 10]
# # numbers.append(even_numbers) # Menambahkan list sebagai elemen baru
# # print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# numbers.extend(even_numbers) # Tidak menambahkan list
# print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# angka = [1, 2, 3, 5, 6]
# print(angka)  # Output: [1, 2, 3, 5, 6]
# angka.insert(3, 4)
# print(angka)  # Output: [1, 2, 3, 4, 5, 6]

# angka.remove(6)
# print(angka)  # Output: [1, 2, 3, 4

# angka.pop()
# print(angka)  # Output: [1, 2, 4]

# angka.clear()
# print(angka)  # Output: []

angka = [3, 1, 4, 2, 5]
angka.reverse()
print(angka)  # Output: [5, 2, 4, 1, 3]
angka_sort = sorted(angka)
angka.sort()
print(angka)  # Output: [1, 2, 3, 4, 5]
print(angka_sort)  # Output: [1, 2, 3, 4, 5]4', 'd', 'i', ' ', 's', 'a', 'i', '