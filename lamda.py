# Tanpa lamda
# def square(num):
#     return num ** 2

# print(square(5))  # Output: 25

# Dengan lamda
# numbers = lambda num: num ** 2
# print(numbers(5))  # Output: 25

# angka = [1, 2, 3, 4, 5]

# result = list(filter(lambda x : x % 2 == 0, angka))
# print(result)  # Output: [2, 4]


# sequence = lambda x: x ** 2
# sequence_numbers = list(map(sequence, angka))
# print(sequence_numbers)  # Output: [1, 4, 9, 16, 25]

def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n') # Split per line
    for line_index, line in enumerate(lines): #
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
    return secret_code

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

print(pin_extractor(poem))
