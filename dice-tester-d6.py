test_string  = "636421536214241544266115336244236252363612643144311233244361425445525141543251152523162364242535331622165143312463121632645126464341531452361636135522146513556441233644632315155444316544366256332216152236333563531256612256642125643515623351254564626561354244222543212324611636343565342"
filtered_test_string=[]
d            = 6 #number of sides, only currently works for 6
output       = [0,0,0, 0,0,0]

test_strint = input("input:")

for a in test_string:
  if(a.isdigit() and 1 <= int(a) <= d):
    filtered_test_string.append(a)

test_string = filtered_test_string

for a in test_string:
  output[int(a)-1] += 1

count = 1
for a in output:
  print(f"side{count}: {a}")
  count += 1
  

# to improve myself I promted ChatGPT "what is a better way to write this code:". its output:
"""
You can make the code more concise and readable by using Python's built-in functions and list comprehensions. Here's an improved version of your code:
"""
test_string = "6364215362142415442661153362442362523636126431443112332443614254455251415432511525231"
d = 6  # number of sides, only currently works for 6
output = [0] * d

filtered_test_string = [a for a in test_string if a.isdigit() and 1 <= int(a) <= d]

for a in filtered_test_string:
    output[int(a) - 1] += 1

for count, a in enumerate(output, start=1):
    print(f"side{count}: {a}")

"""
In this improved version:

1.    We use list comprehensions to filter and create filtered_test_string based on your criteria.
2.    We initialize the output list with zeros using a list comprehension.
3.    We use the enumerate function to iterate through output and print the results.

This code accomplishes the same task but is more concise and Pythonic.
"""
