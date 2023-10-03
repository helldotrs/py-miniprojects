input = "foobar"
output_len = 32

def convert_to_binary(string):
    binary_result = ""
    for char in string:
        ascii_code = ord(char)  # Get the ASCII code of the character
        if ascii_code % 2 == 0: 
            binary_result += '0' 
        else:
            binary_result += '1'  # If odd, append '1' to the result string
    return binary_result

def adjust_len(string):
    if len(string) < output_len:        
        adjusted = string.ljust(output_len, '0') #zero padding, fix
        
    elif len(string) > output_len: # If the binary string is longer than the desired length, truncate it
        adjusted = adjusted[:len]

    else
        adjusted = string
        
    return adjusted

