#Task: write a Python program that takes a sentence as input and counts the frequency of each word in the sentence. The program should ignore punctuation and consider words case-insensitively. Output the word frequencies as a dictionary where keys are the words and values are the corresponding frequencies

input_string  = "Hello, world! This is a beautiful world."

input_string = input_string.lower()
print (input_string)

word_list = [word in input_string.split()]
print (word_list)
