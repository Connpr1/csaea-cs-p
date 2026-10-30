# Python functions are blocks of code that can be refused.
# To run a function you call its name followed by parenthisies and any argument it needs

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()
say_hi()
say_hi()
say_bye()

# Functions are more commonly return values not prints
# We can pass this argument into a functions paramiter

def express_this(e): # e is called a parameter it is a placeholder for the argument
    return e

expression = express_this(1 + 2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER

print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("JOJO")
second = greeter("BIZBO")
third = greeter("TONY")

print(first, second, third)

def remainder(a,b):
    return a % b

result = remainder(10,9)
print(result)

def is_far(distance):
    
    if distance < 100 and distance > 20:
        return "Thats not far"
    if distance < 20:
        return "Thats close"
    if distance >= 100:
        return "Thats really far"

distance1 = is_far(38)
distance2 = is_far(79)
distance3 = is_far(1)
distance4 = is_far(400)

print(distance1, distance2, distance3, distance4)

print()

# Challenge 1 make  doubler that doubles the number the amount of times and than puts them in a list.

def doubler(num,time):
    doubled_numbers = []

    for n in range(time):
        num = num * 2
        doubled_numbers.append(num)
        print(doubled_numbers)

    print(doubled_numbers)
    return doubled_numbers
doubler(1, 5)

# Challenge 2 Calculator
def sub (c,d):
    print(c - d)
    return c - d
sub(2,1)

def mult (a,d):
    print(a * d)
    return a * d
mult(3,6)

def div (e,f):
    print(e / f)
    return e / f
div(6,2)

#Challenge 3 Average

def avg (a,b,c,d,e):
    sum = a + b + c + d + e
    quot = sum / 5
    print(f"The average is: {quot}")
    return avg
avg(2,5,6,7,2)

even_odd = int(input("input one number:"))

if even_odd % 2 == 1:
    print("odd")
else:
    print("even")
