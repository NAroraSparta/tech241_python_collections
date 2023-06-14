```python
# Define a list with some cool things inside. E.g. things you would buy if you were a millionaire. The list must have at least 5 elements.
millionaire_shopping_list = ["mansion", "Superyacht", "private jet", "jewellery", "art collection"]

# First, print the list and check it's type
print(type(millionaire_shopping_list))

# Print the list's first element
print(millionaire_shopping_list[0])

# Print the list's second element
print(millionaire_shopping_list[1])

# Print the list's last element using negative indexing
print(millionaire_shopping_list[-1])

# Replace the first item in the list
print(millionaire_shopping_list)
millionaire_shopping_list[0] = "Handbags"
print(millionaire_shopping_list)

# Replace another item in the list and print the list
millionaire_shopping_list[2] = "Library"
print(millionaire_shopping_list)

# Add a new item to the list, print the list
millionaire_shopping_list.append("Shoe collection")
print(millionaire_shopping_list)

# Remove an item from the list, print the list
millionaire_shopping_list.remove("Shoe collection")
print(millionaire_shopping_list)

# Remove the last item from the list without specifying what it is (hint, there is a list method to do this)
del millionaire_shopping_list[-1]
print(millionaire_shopping_list)
```

```python

#Next let’s make a program using lists!
# You are going to make a program that helps a waiter with their menu
millionaire_shopping_list = ["mansion", "Superyacht", "private jet", "jewellery", "art collection"]

# 3- 5 starters
# 3-5 mains
# 3-5 desserts
#
# Make a new file called ‘waiter_helper.py’
#
# See the user stories and complete the task accordingly using lists:
#
# User stories:
#
# As a user, I want to be able to see the menu in a formatted way so that I can order my meal.
arora_gourmet_menu = {
    "Starters": ["Nachos", "Spring rolls", "Onion bhaji", "Chicken wings", "Bruschetta"],
    "Mains": ["Mixed green salad", "butter chicken", "Fish and chips", "Veggie Burgers", "Crispy fried chicken pieces" ],
    "Desserts": ["Apple pie with ice cream", 'Tiramisu', 'Chocolate cake']
}
print(arora_gourmet_menu)

# As a user, I want to be able to order three separate times and have my responses added to a list so they are not forgotten.
customer_order_1 = []
order_1 = input("What would you like to order for starter?")
customer_order_1.append(order_1)

order_2 = input("What would you like to order for mains?")
customer_order_1.append(order_2)

order_3 = input("What would you like to order for dessert?")
customer_order_1.append(order_3)
# As a user, I want to have my order read back to me in a formatted way so I know what I ordered.

print(f"{order_1}, {order_2}, {order_3}")
```

```python
# Your Hero Story!
#
# This is all about dictionaries. Note the method I didn’t show in class was .items(). it returns the key values pairs in the dictionary back as a list of tuples. Try it out!
#
# Summary
# Your going to write a story, cut it into section, store the section in a python dictionary!
#
# Tasks
#
# define a dictionary
#
# add your content as values for keys
#
# follow the instruction in the pseudo code below:
#
# **Dictionary basics :D
# **
# 1 - Define a dictionary call story1, it should have the following keys:
# #"start", "middle" and "end"
story_1 = {
    "start": "Long time ago, there lived a girl who loved to read, dream, paint and cook. Her passion was guessing what others had in their minds.",
    "middle": "One day, while trying to guess what her mum was thinking, she started hearing for some calls for help from a woman. She ran outside but didn't see anyone. She then started talking to that woman in her mind. She asked the woman for directions to her location. It wasn't long before she got to the woman. The woman had hurt herself by falling into an empty but concealed well. With her help,the woman was taken out of the well and given medical care. This made her wonder how could she hear someone she had never met. It started occuring every day and she was able to help anyone in need.",
    "end": "In the years that followed, people started calling her for help and she never let anyone down ever!"
}
# 2 - Print the entire dictionary
print(story_1)

# 3 - Print the type of your dictionary
print(type(story_1))

# 4 - Print only the keys
print(story_1.keys())

# 5 - Print only the values
print(story_1.values())

# 6 - Print the individual values using the keys (individually, lots of print commands)
print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

# 7 - Now let's add a new key:value pair.
story_1["hero"]= "Intuitive Aurora"
```




