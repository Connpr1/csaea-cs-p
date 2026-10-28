#Lists in Python
#Lists store multiple values in one variable
#They are ordered, mutable (Changeble), and allow duplicates

empty_list = []

#Create Lists
animals = ["donkey", "Pangolion", "Blobfish"]
numbers = [2,4, 6, 8, 10]
mixed_data = ["piffle", 42, True, 9.99]

print("Animal List:", animals)
print("Numbers List:", numbers)
print("Mixed data type", mixed_data)

#Print third element in animals
print("Animal list 3rd word:", animals[2])
#Print last element in numbers
print("Last number in munbers:", numbers[-1])
# Print the first element in mixed numbers
print("First element:", mixed_data[0])

animals[-1] = "babarusta"
print(animals)

# add elements to the end of the list
animals.append("glass frog")
print(animals)

#Insert element at certain point in index
animals.insert(2, "aye-aye")
print(animals)
animals.insert(1, "camel")

# Remove elements
animals.remove("aye-aye")
print(animals)

# Remove (pop off) last element and save it into a variable
last_animal = animals.pop()
print(last_animal)
print(animals)


# # Challenge 1
# challenge_list = [1, 2, 3, 4, 5, 6]
# print(challenge_list)
# challenge_list2 = challenge_list.pop(2)
# print(challenge_list2)
# challenge_list3 = (int(input("A number:")))
# challenge_list3 = challenge_list2.insert(2, challenge_list3)
# print(challenge_list2)

# ### **Challenge 2: Shopping List Manager**

# # Initialize an empty list called `shopping`.
# # Add three items of your choice using `.append()`.
# # Then insert one extra item at the second position and remove one item of your choice.
# # Finally, print the final shopping list.
shopping = []
shopping.append(""Chicken", "Milk", "Eggs"")
print("Shopping", shopping)
shopping.remove("Milk")
shopping.insert("Ketchup", 1)
print("Shopping:", shopping)

print()

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Numbers:", nums)

print("Length of list:", len(nums))
print("Min:", min(nums))
print("Max", max(nums))
print("Sum:", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)

nums.reverse()
print(nums)

if "cat" in animals:
    print("cat is in the list")
else:
    print("No cat :(")

# Challenge 3

floats = [1.0, 4.9, 8.5, 6.6, 9.9]

print("Length:", len(floats))
print("Minimum:", min(floats))
print("Max:", max(floats))
print("Sum:", sum(floats))