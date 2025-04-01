# Common pdb commands include:
# n (next): Execute the current line and move to the next line in the same function.
# s (step): Execute the current line and step into any function calls.
# c (continue): Continue execution until the next breakpoint or the end of the program.
# p expression: Print the value of the given expression.
# q (quit): Exit the debugger and terminate the program.
# l (list): Show the code around the current line.
# b: Set a new breakpoint.
# For Python versions older than 3.7,
# the equivalent functionality can be achieved using import pdb; pdb.set_trace().
# The breakpoint() function can be customized using the
# PYTHONBREAKPOINT environment variable.
# Setting it to "0" disables breakpoints,
# while an empty string or no setting at all will invoke the debugger as usual.
# It can also be set to call other debuggers or custom functions.
x = 1
for number in 1,2,3,4,5,6,7:
    breakpoint()
    print(f"{x + number}")
