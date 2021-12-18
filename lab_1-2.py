import math

t = 1 # constant 1
x = 1 # number in group list

# calc function
def calc(t, x):
    return ((9 * math.pi * t + 10 * math.cos(x))) / (math.sqrt(t) - math.fabs(math.sin(t))) * math.pow(math.e, x)

# output
print("t = 1\nx = 1")
print("Z = ", calc(t, x))