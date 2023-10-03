output_len = 32

def convert_to_binary(string):
    binary_result = ""
    for char in string:
        ascii_code = ord(char)  # Get the ASCII code of the character
        if ascii_code % 2 == 0: 
            binary_result += '0' 
        else:
            binary_result += '1'  
    return binary_result

def adjust_len(string):
    if len(string) < output_len:
        for i in range(len(string), output_len):
            # Decide whether to add '0' or '1' based on adjacent characters
            if i % 2 == 0:
                string += '0'
            else:
                string += '1'
        adjusted = string[:output_len]  # Truncate the string to the desired length
    elif len(string) > output_len:
        adjusted = string[:output_len]  # If the binary string is longer than the desired length, truncate it
    else:
        adjusted = string
    return adjusted

def hasher(a):
    a = convert_to_binary(a)
    a = adjust_len(a)
    return a

def print_hash(a):
    print(f"hash for {a}: ")
    print(hasher(a))

print_hash("a")
print_hash("foo bar")
print_hash("password123")
print_hash("abcefghijklmnopqrstuvwxyz")
