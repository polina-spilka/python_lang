# Debugging is like being the detective in a crime movie where you are also the murderer.
# Phaha))
#
# Filipe Fortes

#t will seem like it works as you get the prompt you’re expecting.
# I’ll talk more about the phrase “it works” later on,
# as these words are quite possibly the two most dangerous words in programming!
# haha as well

#Error types:
SyntaxError
TypeError
IndentationError
NameError

items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0
for item in items.keys():
     qty = input(f"How many {item}s have you sold? ")
     print(type(qty))
     print(type(items[item]))
     income = income + float(qty) * items[item]
print(f"\nThe income today was £{income:0.2f}")


# Check for errors can be done better in console
#>>> "hello" * 2.5
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'float'