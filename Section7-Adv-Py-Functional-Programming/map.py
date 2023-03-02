
my_list = [1, 2, 3]


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


def multiply_by2_map(item):
    return item * 2


print(list(map(multiply_by2_map, my_list)))
print(my_list)
my_list = list(map(multiply_by2_map, my_list))
print(my_list)
