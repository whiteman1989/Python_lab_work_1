import math

# function with formula
def calc(x):
    if(x >= 0):
        f = 0.5 - math.fabs(x) ** (1./4.)
    else:
        f = (math.sin(x ** 2) ** 2) / (x + 1)
    return f

# user interface
x = float(input("Enter x: "))

if(x >= 0):
    print("x >= 0")
else:
    print("x < 0")
    
print( "F(x) ", calc(x))