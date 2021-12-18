from random import randint

number_list = [randint(1,9) for i in range(3)]

def find_in_range(min, max, int_list):
    ls = int_list
    result = []
    for i in ls:
        if(i >= min and i <= max):
            result.append(i)
    return result

print("new list: ", number_list)
n = int(input("Emter max value in range: "))
print("Filtered list: ", find_in_range(1, n, number_list))