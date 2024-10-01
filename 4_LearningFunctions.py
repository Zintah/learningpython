# Defining a basic function
def greet():
    print("Hello, World!")

# Calling the function
greet()
# Output: Hello, World!

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

# Calling the function with arguments
greet_user("Alice")
# Output: Hello, Alice!


# Function that returns a value
def add_numbers(a, b):
    return a + b

# Storing the returned value in a variable
result = add_numbers(5, 7)
print(result)  # Output: 12

# Function with a default parameter
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without an argument
greet_user()  # Output: Hello, Guest!

# Calling the function with an argument
greet_user("Alice")  # Output: Hello, Alice!

# Function returning multiple values
def get_user_info():
    name = "Alice"
    age = 30
    city = "New York"
    return name, age, city

# Storing the returned values in variables
name, age, city = get_user_info()
print(f"Name: {name}, Age: {age}, City: {city}")
# Output: Name: Alice, Age: 30, City: New York

# Function with variable number of positional arguments
def add_all(*args):
    return sum(args)

# Calling the function with multiple arguments
print(add_all(1, 2, 3))  # Output: 6
print(add_all(4, 5, 6, 7, 8))  # Output: 30

# Function with variable number of keyword arguments
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
print_user_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# Defining a lambda function
multiply = lambda x, y: x * y

# Using the lambda function
result = multiply(3, 4)
print(result)  # Output: 12

#Using Modules

# Importing the module
import math_utils

# Using functions from the module
print(math_utils.add(5, 3))  # Output: 8
print(math_utils.subtract(10, 4))  # Output: 6

# Importing specific functions
from math_utils import add

print(add(7, 2))  # Output: 9

# Note: subtract() is not imported, so this would raise an error:
# print(subtract(7, 2))  # Uncommenting will cause an error

# Importing with an alias
import math_utils as mu

print(mu.add(5, 3))  # Output: 8

# Importing a function with an alias
from math_utils import add as addition

print(addition(10, 5))  # Output: 15


#built in modules

import math

# Using the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793

import random

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Choose a random element from a list
choices = ["apple", "banana", "cherry"]
print(random.choice(choices))

