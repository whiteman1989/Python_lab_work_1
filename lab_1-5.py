from random import randint

# data
number_list = [randint(1,100) for i in range(3)]

# logic
def find_min_or_max(n, num_list):
    ls = list(num_list)
    result = 0
    if(n % 2 == 0):
        result = min(ls)
    else:
        result = max(ls)
    return result

# user interface
print("New list: ", number_list)
n = int(input("Enter you group number: "))
result = find_min_or_max(n, number_list)
if(n % 2 == 0):
    print("min number is: ", result)
else:
    print("max number is: ", result)
