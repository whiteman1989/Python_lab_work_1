import math

t = float(input("Enter t: "))
x = float(input("Enter x: "))

# calc function
def calc(t, x):
    return ((9 * math.pi * t + 10 * math.cos(x))) / (math.sqrt(t) - math.fabs(math.sin(t))) * math.pow(math.e, x)

# output
print("t = 1\nx = 1")
z = calc(t, x);
print("Z = ", "{0:.2f}".format(z))