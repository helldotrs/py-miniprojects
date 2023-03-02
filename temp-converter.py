#written 2023 by hellmak.com
#verbose code for ease for writing/reading

#fixme: google translate approch, but celcium instead of endlish?

def f2c(a): 
    a = a - 32
    a = a * 5
    a = a / 9
    return a

def k2c(a):
    a = a - 273.15
    return a

def c2k(a):
    a = a + 273.15
    return a

def c2f(a):
    a = a * 1.8
    a = a + 32 
    return a
    #interesting fact about fahrenheit, 100 was supposed to be body pemperature but Daniel Gabriel Fahrenheit had a fever when he messured it. 


input_var = float(input("input number, dot [.] for decimal:"))

print(f"{input_var}c --> {c2f(input_var)}f")

print(f"{input_var}f --> {f2c(input_var)}c")

print(f"{input_var}k --> {k2c(input_var)}c")
print(f"{input_var}c --> {c2k(input_var)}k")
