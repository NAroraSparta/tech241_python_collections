# Sets and Frozen Sets

# {} - list but unordered

car_parts = {"wheels", "windows", "exhausts", "steering_wheel"}
print(car_parts)

#add to a set

car_parts.add("doors")
print(car_parts)

#remove from a set

car_parts.remove("doors")
print(car_parts)

#Frozen set

x = frozenset(["one", "two", "three", "four"])
print(x)