# class Example:
#     def __init__(self):
#         self._internal = "This is a mangled attribute"
#         self.__private = "This is a private attribute"

# obj = Example()
# print(obj._internal)          # Accessing the non-mangled attribute
# print(obj.__private)  # Accessing the private attribute using name mangling


# class Example:
#     def __init__(self, internal, private):
#         self._internal = internal
#         self.__private = private

# obj = Example("This is a mangled attribute", "This is a private attribute")

# print(obj.__dict__)

class Parent:
    def __init__(self):
        self.__data = "Sensitive Data"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = "Child's Sensitive Data"

c = Child()
# p = Parent()
print(c.__dict__)  # Output: {'_Parent__data': 'Sensitive Data', '_Child__data': "Child's Sensitive Data"}
# print(p.__dict__)  # Output: {'_Parent__data': 'Sensitive Data'}