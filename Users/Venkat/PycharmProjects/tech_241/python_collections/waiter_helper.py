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