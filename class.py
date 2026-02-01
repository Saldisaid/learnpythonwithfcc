# class ClassName:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sample_method(self):
#         print(self.name.upper())


# obj = ClassName("example", 30)
# print(obj.name)

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name.upper()} says Woof!")

# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)

# dog1.bark()
# dog2.bark()

# Contoh Instance & Class Attribute

# class Dog:
#     species = "Canis familiaris"  # Class Attribute

#     def __init__(self, name):
#         self.name = name  # Instance Attribute

#     def bark(self):
#         return f"{self.name.upper()} says Woof!"


# print(Dog.species)
# dog1 = Dog("Buddy")
# print(dog1.name)
# print(dog1.species)
# print(dog1.bark())


# dog2 = Dog("Max")
# print(dog2.name)
# print(dog2.species)
# print(dog2.bark())


# class Car:
#     def __init__(self, color, model):
#         self.color = color  # Instance Attribute
#         self.model = model  # Instance Attribute

#     def describe(self):
#         return f"This car is a {self.color} {self.model}."

# car1 = Car("Red", "Sedan")
# car2 = Car("Blue", "SUV")

# print(car1.color)
# print(car1.model)
# print(car1.describe())
        
# print(car2.color)
# print(car2.model)
# print(car2.describe())

# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
    
#     def __len__(self):
#         return self.pages
    
#     def __str__(self):
#         return  f"'{self.title}' with {self.pages} pages"
    
#     def __eq__(self, other):
#         return self.pages == other.pages


# book1 = Book("Python Programming", 350)
# book2 = Book("Data Science", 450)

# print(len(book1))
# print(str(book2))
# print(book1 == book2)

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add(self, item):
#         self.items.append(item)

#     def remove(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print(f"{item} is not in chart")

#     def list_items(self):
#         return self.items
    
#     def __len__(self):
#         return len(self.items)
    
#     def __getitem__(self, index):
#         return self.items[index]
    
#     def __contains__(self, item):
#         return item in self.items
    
#     def __iter__(self):
#         return iter(self.items)
    

# card = Cart()
# card.add("Laptop")
# card.add("Wireless")
# card.add("Mouse")
# card.add("Keyoard")

# for item in card:
#     print(item, end=' ')

# print(len(card))
# print(card[3])

# print('Monitor' in card)
# print('Mouse' in card)

# card.remove('Wireless')
# print(card.list_items())

# card.remove('Laptop')
    
### getattr
# class Person:
#     def __init__(self, name, age, tolis):
#         self.name = name
#         self.age = age
#         self.tolis = tolis

# # attr_name = input('Enter the attribute you want to see: ')
# person = Person('Saldi', 27, 'tolis')
# # print(getattr(person, 'name'))
# # print(getattr(person, 'age'))
# # print(getattr(person, 'city', 'Makassar'))
# # # print(getattr(person, attr_name, "Tidak ada"))

# for attr in dir(person):
#     if not attr.startswith('__') and not callable(getattr(person, attr)):
#         print(f"{attr}: {getattr(person, attr)}")



# # # Setattr
# class Configuration:
#     pass

# settings_data = {
#     'server_url': 'https://api.example.com',
#     'timeout_sec': 30,
#     'max_retries': 5
# }

# config_obj = Configuration()

# for attr_name, attr_value in settings_data.items():
#     setattr(config_obj, attr_name, attr_value)

# print(config_obj.server_url)
# print(config_obj.timeout_sec)



# ## hasattr

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# product_a = Product('T-shirt', 25)

# required_attributes = ['name', 'price', 'inventory']

# for attr in required_attributes:
#     if not hasattr(product_a, attr):
#         print(f"ERROR: Product is missing the required attribute: '{attr}'")
#     else:
#         print(f'{attr}: {getattr(product_a, attr)}')
        

# # ## delattr

# class UserSession:
#     def __init__(self, user_id, token):
#         self.user_id = user_id
#         self.auth_token = token
#         self.temp_counter = 0

# session = UserSession(101, 'a1b2c3d4e5')

# attr_to_clean = ['auth_token', 'temp_counter']

# for attr in attr_to_clean:
#     if hasattr(session, attr):
#         delattr(session, attr)
#         print(f'Removed attribute: {attr}')


# for attr in dir(session):
#     if not attr.startswith('__') and not callable(getattr(session, attr)):
#         print(f' - {attr}: {getattr(session, attr)}')



class Menu:
    dish_of_the_day = "spam"

print(Menu.dish_of_the_day)

class Dog:
    def __init__(name, age):
        self.name = name
        self.age = age

dog = Dog("Pinky", 3)
print(dog.name)




















































































