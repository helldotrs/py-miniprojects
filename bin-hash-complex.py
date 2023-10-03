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

def add_padding(string, count_zeros, count_ones):
    # Add 1 if there are more 1s, else add 0
    if count_zeros > count_ones:
        padded_string = string.ljust(output_len, '1')
    else:
        padded_string = string.ljust(output_len, '0')
    return padded_string

def compress_string(string, count_zeros, count_ones):
    # Create a compressed string with alternating 0s and 1s
    compressed_string = ''.join(['0' if i % 2 == 0 else '1' for i in range(output_len)])
    
    # Replace the alternating bits with the counted 0s and 1s
    compressed_string = compressed_string[:count_zeros] + compressed_string[output_len - count_ones:]
    return compressed_string

def adjust_len(string):
    current_len = len(string)
    count_zeros = string.count('0')
    count_ones = current_len - count_zeros
    
    if current_len < output_len:
        adjusted = add_padding(string, count_zeros, count_ones)
    elif current_len > output_len:
        adjusted = compress_string(string, count_zeros, count_ones)
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
print_hash("b")
print_hash("c")
print_hash("foo bar")
print_hash("password123")
print_hash("abcefghijklmnopqrstuvwxyz")
print_hash("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
