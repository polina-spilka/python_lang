#The bool() function in Python converts a value to a Boolean (True or False).
# It uses the standard truth testing procedure, returning False
# if the argument is omitted, False, 0, None, or
# an empty sequence or collection (e.g., "", [], {}). Otherwise, it returns True

print(bool([]))
print(bool([1,2,3]))

print(bool(False))
print(bool(True))

print(bool())
print(bool(0))
print(bool(None))