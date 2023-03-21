from itertools import combinations

list1 = []
list2 = [3, 2, 1]
target = 1

combs = list(combinations([3, 5, 6, 7], 3))

for i in combs:
    print(sum(i))
    if sum(i) >= target:
        list1.append(sum)

print(list1)
