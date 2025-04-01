file = open("words in pride and prejudice.csv","w")

file.write("Word, Frequency,\n")

# Loop through dictionary and write key-value pairs to csv
for word, frequency  in word_frequencies.items():
    file.write(f"{word},{frequency}")
file.close()

