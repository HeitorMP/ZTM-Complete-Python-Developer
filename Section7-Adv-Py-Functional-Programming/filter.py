
my_list = [1, 2, 3]


def check_odd(item):
    return item % 2 != 0


print(my_list)
print(list(filter(check_odd, my_list)))
