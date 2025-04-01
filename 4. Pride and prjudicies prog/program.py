file = open("pride_and_prejudice.txt")
print(file)
print(file.readline())
print(file.read())

#the two ways of closing the file:
#1.
file.close()
#2.
with open("pride_and_prejudice.txt") as file:
    text = file.read()
print(text)



