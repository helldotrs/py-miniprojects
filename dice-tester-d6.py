test_string  = "6364215362142415442661153362442362523636126431443112332443614254455251415432511525231"
filtered_test_string=[]
d            = 6 #number of sides, only currently works for 6
output       = [0,0,0, 0,0,0]

for a in test_string:
  if(a.isdigit() and 1 <= int(a) <= d):
    filtered_test_string.append(a)

test_string = filtered_test_string

for a in test_string:
  output[int(a)-1] += 1

print(output)
