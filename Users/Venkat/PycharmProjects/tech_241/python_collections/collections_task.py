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




