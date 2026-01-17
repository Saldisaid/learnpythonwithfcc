# Local Scope
# def my_func():
#     var = 10
#     print(var)

# my_func()

# print(var)


# Enclosing Scope

# def outer_func():
#     msg = "Hello"

#     def inner_func():
#         print(msg)
    
#     inner_func()

# outer_func()

# def outer_function():
#     msg = "Hello, World!"
#     res = ""

#     def inner_function():
#         nonlocal res
#         res = "from innner"
#         print(f"Inner: {msg} {res}")
    
#     inner_function()

# outer_function()

# Global Scope
var = "I am global"

def my_function():
    global var2
    var2 = "I am local"
    print(var)

my_function()
print(var)
print(var2)  # This will raise an error because var2 is not defined globally