import math

print("=" * 40)
print("Problem 1")
print("=" * 40)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Welcome {name}")
print(f"Next year you will be {age+1} years old.")

print("=" * 40)
print("Problem 2")
print("=" * 40)
first_number = float(input("Enter number 1: "))
second_number = float(input("Enter second number: "))

print(f"Sum: {first_number+second_number}")
print(f"Difference: {first_number-second_number}")
print(f"Multiply: {first_number*second_number}")

if second_number != 0:
    print(f"Division: {first_number/second_number}")
else:
    print("Cannot be divided by zero")

print("=" * 40)
print("Problem 3")
print("=" * 40)
marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
    gpa = 4.0
elif marks >= 80:
    grade = "A"
    gpa = 3.7
elif marks >= 70:
    grade = "B"
    gpa = 3.0
elif marks >= 60:
    grade = "C"
    gpa = 2.0
else:
    grade = "F"
    gpa = 0.0

print(f"Grade: {grade}")
print(f"GPA: {gpa}\n")

print("=" * 40)
print("Problem 4")
print("=" * 40)
num_to_check = int(input("Enter a number to check: "))

if num_to_check % 2 == 0:
    print(f"{num_to_check} is Even.\n")
else:
    print(f"{num_to_check} is Odd.\n")

print("=" * 40)
print("Problem 5")
print("=" * 40)
radius = float(input("Enter the radius of the circle: "))

# Using formulas: Area = πr², Circumference = 2πr
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
