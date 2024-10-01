#Master Control Flow Statements

# Simple if statement
age = 20

if age >= 18:
    print("You are an adult.")
# Output: You are an adult.

# if-else statement
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Output: You are a minor.

# if-elif-else chain
age = 20

if age < 13:
    print("You are a child.")
elif 13 <= age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
# Output: You are an adult.

# Nested if statement
age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")
# Output: You can drive.

# One-line conditional statement
is_raining = True
weather = "Stay inside." if is_raining else "Go outside."
print(weather)
# Output: Stay inside.


# Looping over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Looping with range() function
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# while loop example
count = 0

while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4

# Iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 30
# city: New York

# break out of a loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# skip the current iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4

# do nothing, often used as a placeholder
for i in range(5):
    if i == 3:
        pass  # Do nothing
    else:
        print(i)
# Output:
# 0
# 1
# 2
# 4

# The else block won't execute if the loop breaks early
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed.")
# Output:
# 0
# 1
# 2


# Nested loops example
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Output:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# i: 1, j: 1
# i: 2, j: 0
# i: 2, j: 1
