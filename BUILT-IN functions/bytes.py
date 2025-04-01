# A string will be encoded into bytes using the specified encoding (default is ‘utf-8’).
# An iterable will have each element converted into bytes but it must have integers between 0 and 255.
# An integer creates a bytes object of that size with all elements initialized to 0.

print(bytes("hi!", "UTF-8"))
print(bytes([1,2,3,4,5]))
print(bytes(3))