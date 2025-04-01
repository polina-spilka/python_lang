# difference between tuples and lists
my_tuple = (1,2,3,4,4,5)
print(my_tuple)
print(type(tuple))

my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))

#tuples can be sliced same as lists
print(my_tuple[2:])
print(my_tuple[-1]) # last element in the list

#tuples are iterable
for i in my_tuple:
    print(i)

#tuples can be written without parentheses
my_second_tuple = 1,2,3,4,5
print(my_second_tuple)
print(type(my_second_tuple))

#Same as list, tuple can contain any data types simultaneously
my_third_tuple = (1,"test", 1.08, True, [1,2], (1,2))
print(my_third_tuple)





# tuples do not support reassignment of its members as lists do
my_tuple[2] = 666








