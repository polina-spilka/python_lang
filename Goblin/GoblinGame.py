import random
#this is my first program on python so far
number_of_dors = 20

print("Welcome to the angry Goblin Hunt")
print("An award-winning game full of adventure and exitement")
player_name = input("What's your name")
print(player_name + ", can you find the Goblin?")
print("|_|"*number_of_dors)
goblin_position = random.randint(1,number_of_dors)
keep_trying=True
while keep_trying==True:
    guessed_position = input("Can you guess where the Goblin is hiding?")
    if goblin_position == int(guessed_position):
        print("Great, you've found the Goblin!")
        keep_trying=False
    else:
        print("No, sorry the Goblin is still hiding somewhere!")

print("Thank you for playing, Now it's time to go back to work!")
