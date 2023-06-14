# Lists(Arrays) and Tuples

```python

Python Lists:

Lists are used to store multiple items in a single variable.
Lists are one of 4 built - in data types in Python used to store
collections of data, the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.
Lists are created using square brackets.
```
```python
# Making a list in Python
#List items are ordered, changeable, and allow duplicate values.

#List items are indexed, the first item has index [0], the second item has index [1] etc.

shopping_list = ["eggs", "bacon", "bananas", "bread", "milk"]
print(type(shopping_list))
print(shopping_list)
```
```python
Accessing certain parts of List

print(shopping_list[-3])
```
```python
# change a specific element of my list

shopping_list[4] = "Orange Juice"
print(shopping_list)
```
```python
# list methods
#When we say that lists are ordered, it means that the items have a defined order, 
#and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

shopping_list.append("butter")
print(shopping_list)
print(shopping_list[5])
shopping_list.remove("butter")
print(shopping_list)
```
```python
The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.

shopping_list.pop()  # gets rid of the last one in the list
print(shopping_list)

shopping_list.pop(0)
print(shopping_list)
```
```python
# Mixed data type list

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

# list slicing

print(mixture[1:3])  # 2,3

print(mixture[::2])  # skips over 1 and prints the other # [1, 3, 'two']
```

```python
# Tuples
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))
```
```python
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
```

```python
# Tuples
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))
```
```python
Sets and Frozen Sets

# {} - list but unordered

car_parts = {"wheels", "windows", "exhausts", "steering_wheel"}
print(car_parts)

#add to a set

car_parts.add("doors")
print(car_parts)

#remove from a set

car_parts.remove("doors")
print(car_parts)
```

```python
#Frozen set
In Python, a frozen set is an immutable, hashable collection of unique elements. 
It is similar to a set but with the key difference that once a frozen set is created, 
its elements cannot be modified. This immutability makes frozen sets suitable 
for use as keys in dictionaries and elements in other sets.

x = frozenset(["one", "two", "three", "four"])
print(x)
```
```python
Dictionaries

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets.

# Key - Value pairs

# Key is the name/reference, value is the data stored.

# Makinga a dictionary

student_1 = {
    "name": "Neha",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["variables", "git", "data_types", "collections"]
}

print(type(student_1))

#How to access parts of a dictionary
print((student_1["stream"]))

print((student_1["completed_lessons_names"][:2]))

#Changing a value

student_1["completed_lessons_names"] = "data_analytics"
print(student_1["stream"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())
```

