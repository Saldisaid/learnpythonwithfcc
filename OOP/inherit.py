# class Parent:


# class Child(Parent):


# Single Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return f"{self.name} makes a sound."
    
class Dog(Animal):
    bark = "Woof!"

    def sound(self):
        base = super().sound()
        return f"{base} and {self.name} barks {self.bark}"

jack = Dog("Jack")
print(jack.name)  # Output: Jack
print(jack.sound())  # Output: Jack makes a sound. and Jack barks Woof!
print(Dog.bark)  # Output: Woof!

# Multiple Inheritance Example

class Walker:
    def walk(self):
        return f"{self.name} is walking."

class Swimmer:
    def swim(self):
        return f"{self.name} is swimming."
    
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}, i can {self.walk()} and {self.swim()}"

frog = Amphibian("Froggy")
print(frog.introduce())  # Output: I am Froggy, i can Fro
    
















