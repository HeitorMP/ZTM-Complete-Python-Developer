# Exercise: Check for duplicates in list:
# set type is forbidden


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# My first solution
dup_list = []
for item in some_list:
    for index in range(0, len(some_list)):
        if item == some_list[index] and some_list.index(item) != index and item not in dup_list:
            dup_list.append(item)

print(dup_list)

# Better solution from teacher!
# use the .count method to check the occurrence of the element in the list
# more clean and just one loop
another_dup_list = []

for item in some_list:
    if some_list.count(item) > 1 and item not in another_dup_list:
        another_dup_list.append(item)

print(another_dup_list)
