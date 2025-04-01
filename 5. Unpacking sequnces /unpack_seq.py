#unpack tuple
me,you = ("Polina", "Leha")
print(me)
print(you)

#unpack dictionary
dict = {"bad":1,"good":2,"average":3}
list_of_tuples = dict.items()
for tuple in list_of_tuples:
    print(tuple)

#unpack dictionary to tupels list and immediately unpack tuple to two vars
for state, place in dict.items():
    print(state)
    print(place)



