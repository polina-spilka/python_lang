import random

#prints random values until the value greater than 20 is found
stop_value = 0
while stop_value < 20:
    print(stop_value)
    stop_value=random.randint(1, 30)
print(f"{stop_value} - you've found number greater then 20")