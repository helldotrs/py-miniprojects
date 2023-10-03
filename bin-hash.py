input = "foobar"

def convert_to_binary(string):
    binary_result = ""
    for char in string:
        ascii_code = ord(char)  # Get the ASCII code of the character
        if ascii_code % 2 == 0: 
            binary_result += '0' 
        else:
            binary_result += '1'  # If odd, append '1' to the result string
    return binary_result


