#Lists
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Modifying a list
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Removing elements
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Slicing a list (extracting sublists)
print(fruits[0:2])  # Output: ['apple', 'blueberry'] (elements at index 0 and 1)
print(fruits[-1])   # Output: orange (last element)


#Tuples (Immutable)
# Creating a tuple
coordinates = (10, 20)

# Accessing tuple elements
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20

# Tuples are immutable, so this will raise an error:
#coordinates[0] = 30  # Uncommenting this will cause an error

#TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
coordinates = (30, 40)
print(coordinates)  # Output: (30, 40)


#Sets
# Creating a set
colors = {"red", "green", "blue"}

# Adding elements
colors.add("yellow")
print(colors)  # Output: {'red', 'green', 'blue', 'yellow'}

colors.add("yellow")
print(colors) #ignores adding the 2nd yellow

# Removing elements
colors.remove("green")
print(colors)  # Output: {'red', 'blue', 'yellow'}

# Checking membership
print("red" in colors)  # Output: True
print("purple" in colors)  # Output: False

# Set operations (union, intersection, difference)
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection: {3}
print(set_a - set_b)  # Difference: {1, 2}



#Dictionaries

# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values by keys
print(person["name"])  # Output: John
print(person["age"])   # Output: 30

# Modifying a value
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
person["job"] = "Developer"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'job': 'Developer'}

# Iterating over dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 31
# job: Developer


# List of dictionaries
people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Accessing data
for person in people:
    print(f"{person['name']} is {person['age']} years old.")
# Output:
# Alice is 28 years old.
# Bob is 25 years old.
# Charlie is 35 years old.
