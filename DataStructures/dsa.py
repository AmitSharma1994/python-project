# 1. Lists
# creating the List
from tkinter.font import names

fruits = ["apple", "oragnge", "cherry"]
print(fruits)

# accessing the list
for i in range(2):
    print(fruits[i])

fruits.append("banana")

print(fruits)
fruits.reverse()
print(fruits)
fruits.remove("apple")
print(fruits)

# iterating the list

for fruit in fruits:
    print(fruit)

# 2. Tuples Creating a tuple
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Accessing elements by index
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20

# Tuples are immutable, so you cannot modify them
# coordinates[0] = 15  # This will raise a TypeError

# 3. Dictionaries Creating Dictionaries:

studentDic = {"name": "Alice", "Age": "24", "country": "India", "salary": "20000"}

print(studentDic)

print(studentDic["name"])
print(studentDic["Age"])
print(studentDic.get("Age"))

# Iterating Through Dictionaries:

for stu in studentDic:
    print(stu, studentDic[stu])

# Iterating through key-value pairs

for key, val in studentDic.items():
    print(key, val)
#4.Sets
#Creating Sets:
colors = {"red","green","orange","vialate"}
print(colors)

#Set Operations:

# Adding elements
colors.add("yellow")
print(colors)  # Output: {'red', 'green', 'blue', 'yellow'}

# Removing elements
colors.remove("green")
print(colors)  # Output: {'red', 'blue', 'yellow'}

# Checking membership
print("red" in colors)  # Output: True
print("green" in colors)  # Output: False

#Set Operations (Union, Intersection, Difference):

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}
print(set2 - set1)  # Output: {4, 5}