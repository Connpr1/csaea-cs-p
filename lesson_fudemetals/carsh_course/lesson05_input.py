import math

# USER INPUT IN PYTHON
#print("PROMT")
# print()

# name = input("Enter your name:")
# print(f"Hello, {name}")

# print(type(name))

# age = input("Enter your age:")
# print(f"Your age is, {age}")

# print(type(age))

# age_converted = int(age)
# print(type(age_converted))

# height = float(input("Enter your height:"))
# print(f"You are {height} cm tall")
# print(height + 1)
# print("\n\n")

#Challenge 1

# color_fav = input("Enter your favorite color:")
# print(f"Your favorite color is {color_fav}")

# #Challenge 2

# num1 = int(input("Pick a number between 1 and 10: "))

# num2 = int(input("Pick another number: "))
# #final_num = num_1  num_2
# print(f"Both your numbers equal {num1 + num2}")


# #Challenge 3: Circle Area from User Input
# # Ask the user for the diameter of a circle, then calculate and print the area.
# # pi radius squared 

# diameter = int(input("Enter diameter:"))
# raduios = diameter / 2
# area_circle = math.pi * raduios ** 2
# print(f"Area of circle is {area_circle}")


# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random

dice_sides = int(input("How many sided dice: "))
roll = random.randint(1, dice_sides)
print(f"You rolled: {roll}")
