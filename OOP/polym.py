# class Cat:
#     def speak(self):
#         return "Meow!"

# class Bird:
#     def speak(self):
#         return "Chirp!"

# class Monkey:
#     def speak(self):
#         return "Ooh ooh aah aah!"
    
# def animal_sound(animal): 
#     print(animal.speak())

# animal_sound(Cat())    # Output: Meow!
# animal_sound(Bird())   # Output: Chirp!
# animal_sound(Monkey()) # Output: Ooh ooh aah aah!  

class Twitter:
    def __init__(self, content):
        self.content = content
    
    def post(self):
        return f'Tweet {self.content} (140 characters)'
    
class Instagram:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"Instagram post : {self.content} (220 characters)"
    
class LinkedIn:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"LinkedIn post : {self.content} (300 characters)"

def start(platform):
    print(platform.post())

tweet = Twitter('Baru belajar polymorphism Python!')
photo = Instagram('Senja sore 🌅')
article = LinkedIn('Mengapa OOP penting di 2024')

start(tweet)      # Output: Tweet Baru belajar polymorphism Python! (140 characters)
start(photo)     # Output: Instagram post : Senja sore 🌅 (220 characters
start(article)   # Output: LinkedIn post : Mengapa OOP penting di 2024 (300 characters)

# polymorphism with Inheritance
class Animal:
    def speak(self):
        return "Some sound"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
    
print(Animal().speak())  # Output: Some sound
print(Cat().speak())     # Output: Meow!
print(Dog().speak())     # Output: Woof!
print(Cow().speak())     # Output: Moo!

# Polymorphism with Loops list
animal = [Cat(), Dog(), Cow()]

for a in animal:
    print(a.speak())
























