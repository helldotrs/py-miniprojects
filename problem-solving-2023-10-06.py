#Task: write a Python program that takes a sentence as input and counts the frequency of each word in the sentence. The program should ignore punctuation and consider words case-insensitively. Output the word frequencies as a dictionary where keys are the words and values are the corresponding frequencies

import re

def count_words(a):
    a           = re.sub(r'[^\w\s]', '', a) #regex punctuation removal
    a           = a.lower()

    word_list   = a.split()

    word_count  = {word: word_list.count(word) for word in word_list}

    return word_count

def print_count(a):
    print(count_words(a))

print_count("Hello, world! This is a beautiful world.")
