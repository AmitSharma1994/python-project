# 1. Basic Syntax

x = 1
if x == 1:
    # this is print Syntax.
    print("x is 1")
if True:
    print("Hello, WorLd")  # this is indented block
# 2 basic input outout example  Use input() for input. and Use print() for output.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# name = input("Enter your name: ")
# print("hello " + name + "!")
# Output to the user
# print(f"Hello, {name}! You are {age} years old.")
# 3. Variables and Data Types:  Variables are used to store data. You don't need to declare the type explicitly.
# Integer
x = 10  # this is for interger.
print(type(x))
print("example of integer :", x)
# Float
y = 3.14  # this for flot.
print(type(y))  # <class 'float'>
print("example of flot :", y)

# String
name = "alice"  # this is for string.
print(type(name))  # <class 'str'>

print("example of string " + name)  # for sting we can use + and , as well as.

# Boolean
is_student = True  # boolean
print(type(is_student))  # <class 'bool'>

print("example of boolean :", is_student)

# 4. Arithmetic Operators: +, -, *, /, // (floor division), % (modulus), ** (exponentiation)
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333
print(a // b)  # 3
print(a % b)  # 1
print(a ** b)  # 1000

# 5.Comparison Operators:  ==, !=, >, <, >=, <=
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True
print(a >= b)  # False
print(a <= b)  # True
# 6. Logical Operators: and, or, not

# 7. Logical Operators: and, or, not
a = True
b = False

print(a and b)  # False
print(a or b)  # True
print(not a)  # False
# 8. Bitwise Operators: &, |, ^, ~, <<, >>
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1 (0001 in binary)
print(a | b)  # 7 (0111 in binary)
print(a ^ b)  # 6 (0110 in binary)
print(~a)  # -6 (inverts all bits)
print(a << 1)  # 10 (1010 in binary)
print(a >> 1)  # 2 (0010 in binary)
# 8. Assignment Operators:  =, +=, -=, *=, /=, %=, **=, //=
a = 10
a += 5  # a = a + 5
print(a)  # 15

a -= 3  # a = a - 3
print(a)  # 12

a *= 2  # a = a * 2
print(a)  # 24

a /= 4  # a = a / 4
print(a)  # 6.0

a %= 5  # a = a % 5
print(a)  # 1.0

a **= 3  # a = a ** 3
print(a)  # 1.0

a //= 2  # a = a // 2
print(a)  # 0.0

# 9. Control Flow

# 9.1 if -else  statements.

age = 18
if age >= 18:
    print("you are the adult.")
else:
    print("you are not the adult.")

# 9.2 Loops:   For Loop: and while  Loop:

print("example of for loop")
for i in range(5):
    print(i)

print("example of while loop")
count = 0
while count < 5:
    print(count)
    count += 1

# 9.3 control Flow statements: break ,continue, pass.
print("example of break")
for i in range(10):
    if i == 8:
        break
    print(i)
print("example of pass: Does nothing, acts as a placeholder.")
for i in range(10):
    pass
