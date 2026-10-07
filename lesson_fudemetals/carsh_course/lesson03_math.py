#Key concepts math operators (+, _, *, /, //, %, **)

add = 745343 + 24
print("sum:", add)

subtract = 44 - 4
print("Differnce:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("float division:", float_divide)

intiger_divide = 7 // 2
print("Intiger Division:", intiger_divide)

mod = 7 % 2
print("Modulus:", mod)

exponent = 7 ** 2
print("Exponent:", exponent, "\n")

# PEMDAS (Parenthisis, Exponents, Multiplication, Division, Addistion, Subtraction)

result1 = 2 + 3 *4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3, "\n")

# Lesson 03 Challenges
# Calculate the area of a rectangle with a width of 8 and a height of 5.
# Create seperate variables for Width, Height, and Area

w = 8
h = 5
area = 8 * 5
print("Area:", area)

# Challenge 2: Circle Area
# Use the formula 3.14^2 to calculate the area of a circle with the radious of 7
# Seperat variabkes for pi, radious, and result

pi = 3.14
radious = 7
area = pi * 7 ** 2
print("area:", area)

# Challenge 3: Shopping tool
# A book is $12.99 and a notebook costs $3.50
# Calculate the amount of 3 books and 4 notebooks.

book = 12.99
notebook = 3.50
total = book * 3 + notebook * 4
print(f"Your total is ${total}")

# Challenge 4: Even or Odd
# Use the Modulus to print if the number 57 is even or odd
# Bonus use conditional to print if even or odd

challenge = 57
odd = [51, 53, 55, 57, 59]
even = [50, 52, 54, 56, 58]
if challenge == even:
    print("Even")
elif challenge == odd:
    print("Odd")