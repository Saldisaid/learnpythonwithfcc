# import pdb

# def add(a, b):
#     result = a + b
#     print(f"Addition: {a} + {b} = {result}")
#     return result

# def divide(a, b):
#     pdb.set_trace()  # Set a breakpoint here
#     return a / b

# try:
#     x = 10/0
# except ZeroDivisionError as e:
#     print("Error: Division by zero is not allowed.")
#     print(f"Exception details: {e}")


# try:
#     x = 10 / 2
# except ZeroDivisionError as e:
#     print("You can't divide by zero!")
# else:
#     print(f"Division successful: {x}")
# finally:
#     print("Execution completed.")


# try:
#     number = int('abc')
#     result = 10 / number
# except ValueError as ve:
#     print("ValueError: Invalid input. Please enter a valid integer.")
#     print(f"Exception details: {ve}")
# except ZeroDivisionError as zde:
#     print("ZeroDivisionError: You can't divide by zero!")
#     print(f"Exception details: {zde}")

# try:
#     number = int(input("Enter a number: "))
#     result = 10/number
# except (ValueError, ZeroDivisionError) as e:
#     print(f"An error occurred: {e}")

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     return age

# try:
#     check_age(-5)
# except ValueError as ve:
#     print(f"Caught an exception: {ve}")

# def process_data(data):
#     try:
#         result = int(data)
#         return result * 2
#     except ValueError as ve:
#         print("Logging: Invalid data provided.")
#         raise

# try:
#     process_data('abc')
# except ValueError as e:
#     print(f"Handled at higher level: {e}")

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Available balance is {balance}, attempted withdrawal is {amount}.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount






















































































