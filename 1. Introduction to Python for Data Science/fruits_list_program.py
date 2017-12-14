# FRUITS LIST MANIPULATION PROGRAM

print("FRUITS LIST MANIPULATION PROGRAM \n")

fruits = [["Apple", 1],
          ["Orange", 2],
          ["Banana", 3]]

print("This is the fruit list: " + str(fruits) + "\n")

#Access 1 element of list
print("Accessing element in fruits[0] \n")
print(fruits[0])
print("\n")

print("Accessing element in fruits[0][0] \n")
print(fruits[0][0])
print("\n")

#List slicing

#Prints all elements of the list
print("Printing all elements fruits[:] \n")
print(fruits[:])
print("\n")

#Prints list elements from index 0 excluding index 2
print("Printing fruits[0:2] \n")
print(fruits[0:2])
print("\n")

print("Printing fruits[:2] \n")
print(fruits[:2])
print("\n")

#Prints all list elements from index 1
print("Printing fruits[1:] \n")
print(fruits[1:])
print("\n")

#List manipulation

#Change list element
print("fruits[0] was changed to Strawberry and 4 \n")
fruits[0] = ["Strawberry", 4]

print("This is fruits \n")
print(fruits)
print("\n")

#Add element
print("Added Watermelon and 5 \n")
fruits = fruits + [["Watermelon", 5]]

print("This is fruits \n")
print(fruits)
print("\n")

#Delete element
print("Deleted fruits[3] \n")
del(fruits[3])

print("This is fruits \n")
print(fruits)
print("\n")

#fruits and y pointing to the same list
print("y = fruits \n")
print("fruits and y are going to point to the same list \n")
y = fruits

print("y[0] changed to Grape and 6 \n")
y[0] = ["Grape", 6]

#fruits list also changes
print("This is fruits \n")
print(fruits)
print("\n")

print("This is y \n")
print(y)
print("\n")

print("They both changed \n")
print("We want only y to be changed \n")

#To avoid that
print("fruits[0] changed to Apple and 1 \n")
fruits[0] = ["Apple", 1]

print("This is fruits \n")
print(fruits)
print("\n")

print("y = list(fruits) \n")
y = list(fruits)
print("\n")

print("y[0] changed to Mango and 7 \n")
y[0] = ["Mango", 7]

#y changed while fruits did not
print("This is fruits \n")
print(fruits)
print("\n")

print("This is y \n")
print(y)
print("\n")

print("y changed while fruits did not \n")
