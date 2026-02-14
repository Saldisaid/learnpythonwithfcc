"""Abstraksi adalah proses menyembunyikan detail implementasi yang kompleks dan hanya menampilkan fitur penting dari sebuah objek atau sistem. Bayangkan abstraksi seperti memfokuskan pada apa yang dilakukan sesuatu, bukan bagaimana cara kerjanya."""
# from abc import ABC, abstractmethod

# class AbstrctClass:
#     @abstractmethod
#     def abstrct_method(self):
#         pass

# class ConcrteClassOne(AbstrctClass):
#     def abstrct_method(self):
#         print("Implementasi metode abstrak di ConcrteClassOne")

# class ConcrteClassTwo(AbstrctClass):
#     def abstrct_method(self):
#         print("Implementasi metode abstrak di ConcrteClassTwo")


# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.make_sound()

# Abstrak class dengan atribut dan metode abstrak
from abc import ABC, abstractmethod

class TalkingToy(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass

class RobotToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says: Beep Boop!")

class TeddyBearToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says: I love you!")

class DinoToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says: Roar!")


rusdi = RobotToy("Rusdi the Robot")
bella = TeddyBearToy("Bella the Bear")
rex = DinoToy("Rex the Dinosaur")

toys = [rusdi, bella, rex]

for toy in toys:
    toy.speak()






















