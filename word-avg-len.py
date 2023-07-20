import re

def avg_len(in_str):
  number_of_words        = len(in_str.split())
  number_of_alpha_chars  = len(re.sub(r'[^a-zA-Z]', '', in_str))
  return number_of_alpha_chars / number_of_words

print(avg_len("this is a string with some words in it"))
