import math

# comment

# ctr
# foward
# slash

print ("Hello World!")

# Variable Declerations and Data Types:

a = 4          # Intiger
b = 5.5        # Floats
c = "CSAEA"    # Strings
D = False      # Boolean

print(a, b, c, D)


#Operators
# + - / * % ** //
# += -= /= 

e = 11 % 10
print(e)
e += 7
print(e)

# f-string

print(f"e is equal to {e}")

e -= 7
e += 12

print(f"e is NOW equal to {e}")

# COMPARISONS (booleans, which always return True or False)

# < >  <= >=  == !=

print(4 < 5)
print(7 == 4)
print(1 != 2)

isEqual = "Yes" != "yes"
print(isEqual)


# Logical Operators
# In order of precedence: not and or

f = False
t = True

#Predict output
print(not f)             # True
print(f and t)           # False
print(f or t)            # True
print(f or t and not f)  # True

#Casting

g = int(5.5) # Will chop off everything after the decimal
h = str(4)
print(g, h)

# Strings

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2 + s3  # concatination with +
end += ", Cowboy."

print(end + "\n") 

# MATH LIBRARY??
# All the way at top

print(math.sqrt(14))  #Square Root
print(math.ceil(3.65)) #Round Up
print(math.floor(7.43)) # Round Down
print(math.pow(2, 4))   # X^Y

# Conditionals
# if elif else

t = True
f = False

if f: 
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else: 
    print("Reached else")

if 1 > 1 and 1 == 1:
     print("Reached the first condition")
elif 6 == 7 or 3!=3:
       print("Reached second condition")
elif 10!=10:
      print("Reached third condition")       
else:
     print("Reached else")

#LISTS
# a list can hold any type, and can grow or shrink anytime

#Index: 0   1   2  3   4
nums = [34, 52, 3, 64, 32]

print(nums)
print(nums[3]) #Predict
print(nums[0])
print(nums[-1])
print(nums[-3])
print(nums[0] + nums[2])

nums[0] = 64
print(nums)

#Lists Methods
#Special built in methods

words = []

words.append("Word 1")
words.append("Word 2")
words.append("Word 3")
print(words)

words.remove("Word 1")
words.insert(0, "Word 4")
words[1] = "Word 5"
length = len(words)
print(words)
print(length)

# Iteration(Loops)
# A for loop will iterate over a range
# A range is a range of numbers
# # range(stop), range(start, stop), range(start, stop, step)

print()
for i in range(5):
    print(i)

animals = ["Sheep", "Deer", "Moose"]
print(f"List: {animals}")

for animal in animals:
    print(f"We saw {animal}")

nums = [5.1, 2.2, 5.3, 3.4, 8.5]

for n in nums:
    print(n + 1)

#Write a four loop to print each value in list nums

for i in range(len(nums)):
     print(nums[i])

# Debugging
print(len(nums))
print(range(5))

#for i in range(0,5):
#     print(nums[i])

# while loop

#Iterates while a condition is true
#when the condition becomes false, it stops

#x = 5

#while x < 10:
#     print(x)
#     x += 1
#ctrl + c to stop make sure to click the output box

#t = True
#f = False

#while t or f:
#     print("hi")