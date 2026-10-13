# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square Root:", sq_root)

round_up = math.ceil(3.3)
print("Round Up:", round_up)

round_down = math.floor(7.99)
print("Round Down:", round_down)

exponent = math.pow(2,5)
print("Exponent:", exponent)

# Constants are variables that never change and they are written in ALL CAPS
PI = math.pi
print(PI) # It stops because it runs out of memory to use

# Challenge 1
radius = 14 / 2
circle_area = PI * math.pow(radius,2)
print("Area of Circle:", circle_area)


# Python Random Library

# Pythons library is a Pseodrandom Number Generator

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

##seed = 162.59
#seed1 = seed * 40
#seed2 = seed1 / 2
#seed3 = seed2 - 1000
#seed_randomized = math.ceil(seed3)
#print(seed_randomized)

# ANSWERE:
seed = 23436

for n in range(5):
    calcs = seed + 223 * 7 / 7
    print(calcs)
    randint = math.ceil(calcs)
    print(f"Simple random number gen: {randint % 10}")
    seed += 1

# Python random library

import random

random_intiger = random.randint(1,100)
print("Random Intiger:", random_intiger)

random_float = random.random()
print("Random float:", random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]

random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list, "\n\n")

# Challenge 2

die_roll = [1, 2, 3, 4, 5, 6]

random.shuffle(die_roll)

roll = random.choice(die_roll)

print("You rolled a", roll, "\n\n")

#Challenge 3

num = random.randint(1, 75)
numsqrt = math.sqrt(num)
print(math.ceil(numsqrt), "\n\n")


#Challenge 4

dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
