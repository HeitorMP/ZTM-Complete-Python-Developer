some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for item in some_list:
    if some_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)

# using comprehensions to do the same

comp_duplicates = list(
    {item for item in some_list if some_list.count(item) > 1})
print(comp_duplicates)
