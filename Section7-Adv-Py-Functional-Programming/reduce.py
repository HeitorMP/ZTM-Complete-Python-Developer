from functools import reduce

my_list = [1, 2, 3]


def check_odd(item):
    return item % 2 != 0


def multiply_by2_map(item):
    return item * 2


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
print(my_list)


a = 0
for i in range(0, 3):
    a = accumulator(a, my_list[i])
    print(a)
