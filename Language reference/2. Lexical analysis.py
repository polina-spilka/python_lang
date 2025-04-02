#2.1 Line structure:

#2.1.2. Physical lines:

#End of line
# Unix form using ASCII LF (linefeed),
# Windows form using the ASCII sequence CR LF (return followed by linefeed),
# the old Macintosh form using the ASCII CR (return) character.

# PYTHON - standard C conventions for newline characters
# (the \n character, representing ASCII LF, is the line terminator).

#2.1.4. Encoding declarations
    # If a comment in the first or second line of the Python script matches
    # the regular expression coding[=:]\s*([-\w.]+),
    # this comment is processed as an encoding declaration:

    # -*- coding: <encoding-name> -*-
    # vim:fileencoding=<encoding-name>
    # !!! If no encoding declaration is found, the default encoding is UTF-8.
# 2.1.5. Explicit line joining
year =1988
month = 8
day = 17
hour = 1
minute =17
second = 55
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # !You cannot put any comments on other lines then last.
        print("This line is one logic expression")

very_long_name = "aaaaaaaaaaa"\
        "bbbbbbbb"
print(very_long_name)

list = [1,2,3,4,5,6, \
        7,8,9,10]
print(list)
#etcetera

#2.1.6. Implicit line joining
    # Expressions in parentheses, square brackets or curly braces
    # can be split over more than one physical line without using backslashes!!!

    #! and it's okay to put comments on each line then)))
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
my_dict = {"key1":1, #oook
           "key2":2} #ooook
my_tuple = (0, # even this is ok
            1) # even this is ok

# 2.1.8. Indentation¶
    # Indentation is rejected as inconsistent if a source file mixes tabs and spaces
    # in a way that makes the meaning dependent on the worth of a tab in spaces;
    # a TabError is raised in that case.

    # The indentation levels of consecutive lines are used to generate INDENT and DEDENT tokens,
    # using a stack - from it the conclusion can be made that it's important to use straight indentation.



