# class ClassName:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sample_method(self):
#         print(self.name.upper())


# obj = ClassName("example", 30)
# print(obj.name)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says Woof!")

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

dog1.bark()
dog2.bark()