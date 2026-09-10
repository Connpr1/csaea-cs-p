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
print(math.pow(2, 4))   #Squares It