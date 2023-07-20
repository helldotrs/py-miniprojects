import re

def avg_len(in_str):
  number_of_words        = len(in_str.split())
  number_of_alpha_chars  = len(re.sub(r'[^a-zA-Z]', '', in_str))
  return number_of_alpha_chars / number_of_words

x   = "this is a string with some words in it"

print(f"average word length in \"{x}\": {avg_len(x)}")
