# Conditionals in Python
#Comparsisons in Python ==, !=, <, >, <=, >=
# Control flow: if, elif, else
# Logical operators and, or, not

# Boolean Refresher

print(3 == 2)
print("Hello" == "Hi there")
print(7 != 4)
print(4 > 5)

# If
num = 12
if num == 10: # Only runs if condition is true
    print("Your num is equal to 10")
    print(10 + num)

# if else
num = 5
if num <= 12:
    print("Your number is less than or equal to 12")
else:
    print("Your number is greater than 12")

# if elif else
tempurature  = 72
if tempurature > 95:
    print("Its hot")
elif tempurature >= 60:
    print("Its nice")
else:
    ("Its freezing")


print()

x = 2
y = 20

if x == 7:
    print(" X is equal to Y")
elif x > y:
    print("X is greater than Y")
else:
    print("X is less than Y")

# Logical Operators
# Both sides of and must be true or its false
age = 16
has_permission = True

if age >= 16 and has_permission:
    print("You can drive")
else:
    print("You have permission")

# Logical Operators 'or' and 'not'

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Its the weekend")
else:
    print("Its a weekday")

print("---Using 'is' and 'not'---")

if day is not "Monday":
    print("Thank god its not monday")



# Challenge 1

age = (int(input("What is your age:")))

if age < 13:
    print("You can watch PG or G movies")
elif age >= 13 and age < 18:
    print("You can watch PG13 movies")
elif age >= 18:
    print("You can watch any movie")

# Challenge 2: Leap Year
# Rules:
#   - Years divisible by 4 are leap years...
#   - ...unless they're divisible by 100, then they're NOT leap years...
#   - ...unless they're also divisible by 400, then they ARE leap years.
# Example output:
# Enter a year: 1900
# 1900 is not a leap year.
# (Test: 2024 -> leap, 1900 -> not, 2000 -> leap)

year = (int(input("Input a year:")))

if year // 4:
    print("Your year is a leap year")
else:
    print("Your year isnt a leap year")