# lambda expressions: anonymous functions that you will need only once

from functools import reduce


my_list = [1, 2, 3]


def check_odd(item):
    return item % 2 != 0


# def multiply_by2_map(item):
#    return item * 2


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))

print(my_list)
# map multiply by 2 with lambda
# lambda param: action(param)
print(list(map(lambda item: item * 2, my_list)))

# filter check odd with lambda
print(list(filter(lambda item: item % 2 != 0, my_list)))

# reduce accumulator with lambda
print(reduce(lambda acc, item: acc + item, my_list))
