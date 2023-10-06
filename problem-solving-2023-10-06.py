#Task: write a Python program that takes a sentence as input and counts the frequency of each word in the sentence. The program should ignore punctuation and consider words case-insensitively. Output the word frequencies as a dictionary where keys are the words and values are the corresponding frequencies

import re

def remove_punctuation(a):
    return re.sub(r'[^\w\s]', '', a)

input_string  = "Hello, world! This is a beautiful world."

input_string = remove_punctuation(input_string)

print (input_string)

input_string = input_string.lower()
print (input_string)

word_list = []
for word in input_string.split():
    word_list.append(word)

print (word_list)

word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
