import math

fahrenheit = 212
Celcious = (fahrenheit - 32) * 5/9
print("Hello, todays weather is gonna be a hot one at",Celcious)


Attempt =  123456
Password = 12345

if Attempt := Password:
    print("Access Granted")

elif Password != Attempt:
    print("Access Denied")

First = "Tommy"
Last = "R"
From = "Rust"

username = First + Last + From

print(username, "Joined The Game")


minutes_parked = "50 minutes"
block_length = 15
cost_per_block = 1

print("You were parked for",minutes_parked)
print ("You owe",block_length * cost_per_block)

savings = 0
weekly_deposit = 15
goal = 100
week = 0

while savings <= goal:
    savings += 15
    week += 1
    print(week, savings)


speed_limit = 55
speed = 71

if speed <= speed_limit:
    print("Legal")
elif speed > speed_limit:
    print("Not legal")
else:
    print("Whatever")




number = 7
Random = 1

for Random in range (1, 11):
    equals = number * Random
    print(f"{number} * {Random} = {equals}")


students = 23
slices = 2
slices_per_pie = 8

print("slices needed", students * slices)

slices_needed = 46

print("pies needed is", slices_needed / slices_per_pie)

pies_needed = 5.75

print("Total pies needed", math.ceil(pies_needed))



playlist = ["Intro", "Song A", "Song B", "Finale"]

print(playlist [-1],  playlist [1], playlist [2], playlist [0])
