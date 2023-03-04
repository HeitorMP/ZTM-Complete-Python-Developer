def fib(num):  # num = index number
    values = [0, 1]
    for n in range(num):
        yield (values[0])
        temp = values[1]
        values[1] = values[0] + values[1]
        values[0] = temp


# Official solution
"""
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
"""

# list exemple
"""
def fib2(number):
    a = 0
    b = 1
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result
"""
my_li = []
for x in fib(20):
    if x % 2 == 0:
        my_li.append(x)


print(my_li)
