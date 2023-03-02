
def f2c(a): 
    a = a - 32
    a = a * 5
    a = a / 9
    return a
    
print(f2c(100))

def c2f(a):
    a = a * 1.8
    a = a + 32 
    return a

print(c2f(100))
