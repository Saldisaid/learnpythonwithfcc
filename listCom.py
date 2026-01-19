# list = []

# for num in range(1, 21):
#     if num % 2 == 0:
#         list.append(num)

# print(list)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# List Comprehension
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# map function
celcius = [0, 10, 20, 30]

def to_fahrenheit(c):
    return (c * 9/5) + 32

result = list(map(to_fahrenheit, celcius))
print(result)  # Output: [32.0, 50.0, 68.0]

tambah = [1, 2, 3, 4, 5]

def kali(n):
    return n * n

result = list(map(kali, tambah))
print(result)  # Output: [1, 2, 6, 24, 120]

numbers = [5, 10, 15, 20]
total = sum(numbers, start=20)
print(total) # ?