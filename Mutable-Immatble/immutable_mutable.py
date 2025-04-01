#the list variable is changed by itself
list = [1, 2, 3,4]
list.append(6)
print(list)

# the string variable is not changed inside.
str = 'John'
str.upper()
print(str)
#you should reassign it
a = str.upper()
print(a)