# Exercise: Create a function that returns the highest even number from a list!

def highest_even(list):
    list.sort()
    list.reverse()
    for item in list:
        return item if item % 2 == 0 else None


def highest_even_2(list):
    list.sort()
    for index in range(len(list) - 1, -1, -1):
        return list[index] if list[index] % 2 == 0 else None


print(highest_even([1, 2, 10, 4, 5]))
print(highest_even_2([1, 2, 10, 4, 5]))

# Teacher solution: (i think mine is better this time! 😋)
"""
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8]))
"""
