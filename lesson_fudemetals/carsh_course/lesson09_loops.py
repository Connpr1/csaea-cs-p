# Loops in python
#Loops repeat a block of code until they hit a limit
# They exist to help us not rewrite the same code everytime
#There are for loops and while loops

import time

# The for loop
# A for loop repeats a loop in a sequence

animals = ["sheep", "dog", "cow", "goose", "donkey"]

print("\nOur animals:", animals)

for a in animals:
    print("Now im petting a", a)
    #time.sleep(0.5) # This will pause the print for half a second

# We can loop through numbers a specific number of times using range()

for i in range(5):
    print("Counting", i)

# range(Start, stop, step)

for num in range(5, 100, 5):
    print(num)

# Strings are also Iterable, so they can be looped as well

fav_word = "Shenanigans"
letter_list = []

for letter in fav_word:
    print(letter)
    letter_list.append(letter + "!")

print(letter_list)

#Challenge 1
print()
total = 0

for s in range(1,11):
    total += s
print(total)

# While loop
# Repeats while the thing is true
#Avoid your program from becoming immortal

# += add to, -= subtract, = over right

count = 0

while count < 5:
    print(f"Loopin --- we are on the loopin idex #{count}")
    count += 1
# We can also use time here

# user_input = ""
# while user_input != "exit":
#     user_input = input(" Type Exit To Escape")

# Loop Control Statements

for i in range(1,11):

    if i == 3:
        print("Skipping 3")
        continue
    if i == 6:
        print("Breaking at 6")
        break
    if i == 9:
        pass # place holder wont do anything

    print("Number:", i)

# Challenge 2
user_input = ""
while user_input != "7":
    user_input = input("Pick a number:"):
    
