my_list = [1, 2, 3]
your_list = [10, 20, 30]


def check_odd(item):
    return item % 2 != 0


def multiply_by2_map(item):
    return item * 2


print(list(zip(my_list, your_list)))
print(my_list)
print(your_list)
