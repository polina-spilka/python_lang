my_dict = {"kate":89, "dave": 87, "kerry":98}
print(my_dict)
print(type(my_dict))

#dictionary is in some way similar to Map in Java
#you cannot get item by index as in list but you always can get the item by KEY
print(my_dict["kate"])

#dictionaries are mutable
my_dict["kate"] = 5
print(my_dict)

#you can even increment the value:
my_dict["dave"] = my_dict["dave"] + 1
print(my_dict)

#you can add new pair to the dictionary - note that "jeremy" didn't exit at the beginning:
my_dict["jeremy"] = 77
print(my_dict)

#the most recently used methods of dictionary
print(my_dict.keys())
print(my_dict.values())

# you can get the value by key,
# if the key doesn't exist, you won't get error as with square brackets, just nothing
print(my_dict.get("Katya"))
#you can also put a default value as a second argument
# in case the values is not in the dictionary
print(my_dict.get("Katya", "No such value"))

#iteration - gets only keys
for stuff in my_dict:
    print(stuff)



