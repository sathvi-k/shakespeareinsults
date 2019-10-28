# Sathvika Korandla
# October 23, 2019
# This program randomly generates a Shakespearean insult.
# Words in the word banks come from: https://web.mit.edu/dryfoo/Funny-pages/shakespeare-insult-kit.html

import random


# Function that opens a file, reads all the words, adds them to a word bank, and returns the word bank
def make_word_bank(filename, readorwrite):
    word_bank = []
    words_file = open(filename, readorwrite)

    # Read each word, remove newline characters and add word to the word bank
    for word in words_file:
        word = word.lstrip('\n').rstrip('\n')
        word_bank.append(word)

    words_file.close()
    return word_bank


# Make a word bank for each file
adjs1 = make_word_bank("adjs1.txt", "r")
adjs2 = make_word_bank("adjs2.txt", "r")
nouns = make_word_bank("nouns.txt", "r")

# Randomly pick a word from each word bank to compose your insult
picker1 = random.randint(0, len(adjs1)-1)  # list indices start at 0
adj1 = adjs1[picker1]

picker2 = random.randint(0, len(adjs2)-1)
adj2 = adjs2[picker2]

picker3 = random.randint(0, len(nouns)-1)
noun = nouns[picker3]

print("Thou " + adj1 + " " + adj2 + " " + noun + "!")
