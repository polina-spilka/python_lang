import string
with open("pride_and_prejudice.txt") as file:
    text = file.read()

# clean the data by removing the capitalization and punctuation marks
text = text.lower()
for punctuation_mark in string.punctuation:
    text = text.replace(punctuation_mark, " ")
# split string into list of strings containing all words
words = text.split()


####
# PART 2: find words and their frequencies
word_frequencies = {}
for word in words:
    if word not in word_frequencies:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] += 1
print(word_frequencies)
print(f"there are {len(word_frequencies)} unique words in the book")

####
# PART 3: Export words and frequencies to a CSV spreadsheet
with open("words in Pride and Prejudice.csv", "w") as file:
    #write header line
    file.write("Word, Frequency\n")

    # Loop through dictionary and write key-value pairs to csv
    for key, value in word_frequencies.items():
        file.write(f"{key},{value}\n")

file.close()






