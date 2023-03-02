# Create lambda expression that squares a list

my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))

# List sorting by the second element of tuples
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
b = [(0, 2), (4, 3), (9, 9), (10, -1)]

# best i can do for now!
# it got worse than not using lambda!
a = list(map(lambda item: (item[1], item[0]), sorted(
    map(lambda item: (item[1], item[0]), a))))
print(a)

# the offical solution! wow much better!!!
b.sort(key=lambda x: x[1])
print(b)
