# String Manipulation in Python
# built in methods len(), upper(), lower(), capatilize()

# String formating, string concations

last_name = "Hello"
first_name = "Conpr1"
print("Hello", first_name, last_name, "!")
# Concatination
print("Hello" + " " + first_name + " " + last_name + "!")
print(f"Hello, {first_name} {last_name}!")


# 0 1 2 3 4
# H E L L O

second_letter = last_name[1]
print(second_letter)

# String Indexing and Slicing
word = "Super-cali-fragil-istic-expi-ali-docious"

print("\nThe word is", word)
print("First letter is:", word[0])
print("The last letter is:", word[-1])
print("Range of letters(Non-Inclusive):", word[3:7] )
print("First five letters", word[:5]) #No need for a 0
print("Everything after the first five letters:", word[5:])
print("Last seven letters:", word[-7:])
print("Every second character:", word[::2])
print("String in reverse:", word[::-1])

last_name = "Satoru"
length = len(last_name)
print("Length of last name:", length)

print('\n')

# Challenge 1

# quote = input("Insert quote:")
# length_quote = len(quote)
# print(f"{quote}""\nThe length of your quote is ", (length_quote), "\n")

# # Challenge 2

# word = input("Seven character word here:")
# print("2nd through 6th letters are:", word[1:6])

# # Challenge 3

# first_name = input("Enter first name:")
# last_name = input(" Enter last name:")

# print(f"Your full name is: {last_name}, {first_name}")

character = "Mr.. CrAb$"
print("\nLowercase:", character.lower())
print("Uppercase:", character.upper())
print("Capatillize first letter:", character.capitalize())
print("Title format:", character.title())

print()

# Find and replace text
sentence = "Im a goofy goober"
new_sentence = sentence.replace("Im", "You're")
print(sentence)
print(new_sentence)

# Join and Split
groceries = "milk,eggs,bread,butter,peanuts"
print("\nOriginal string:", groceries)

# Split the string into a Python list, based on a 'delimiter'
items = groceries.split(",")
print(items)

# Join a list together into a string
joined = " and ".join(items)
print(joined)

#Challenge 3.5

word = input(" Input a word:")
print("Your word is:", word)
print("Your word lowercase is:", word.lower())
print("Your word uppercase is:", word.upper())
print("Word backwords is:", word[::-1])