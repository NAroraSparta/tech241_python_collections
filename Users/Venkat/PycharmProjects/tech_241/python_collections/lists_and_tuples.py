# Lists(Arrays) and Tuples

# Making a list in Python

shopping_list = ["eggs", "bacon", "bananas", "bread", "milk"]
print(type(shopping_list))
print(shopping_list)

# Accessing certain parts of List

print(shopping_list[-3])

# change a specific element of my list

shopping_list[4] = "Orange Juice"
print(shopping_list)

#list methods

shopping_list.append("butter")
print(shopping_list)
print(shopping_list[5])
shopping_list.remove("butter")
print(shopping_list)

shopping_list.pop()         #gets rid of the last one in the list
print(shopping_list)

shopping_list.pop(0)
print(shopping_list)

#Mixed data type list

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

#list slicing

print(mixture[1:3])   #2,3

print(mixture[::2])   #skips over 1 and prints the other # [1, 3, 'two']

# Tuples
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))



