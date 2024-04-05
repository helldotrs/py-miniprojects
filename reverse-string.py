def reverse(str_in):
    str_out = ""
    for char in str_in:
        str_out = char + str_out
    return str_out

my_string = input("reverse:")

print(reverse(my_string))
