x = 1 + 2 * 3 - 4 / 5
list1 = [1, 2, 3, 4, 5]
dict1 = {'a': 1, 'b': 2, 'c': 3}

def calculate_sum_of_squares(val1 = 0, val2 = 0):
    return val1**2 + val2**2

result = calculate_sum_of_squares(2, 3)
if 10 < result < 20:
    print("Result in range")
else:
    print("Result not in range")