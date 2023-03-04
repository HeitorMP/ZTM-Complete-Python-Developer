# Error Handling


while True:
    try:
        age = int(input('What is your age?:'))
        10/age
        raise ValueError('hey cut it out')
    except ZeroDivisionError:
        break

print('Prograns goes on!')

""" 

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('something is wrong! ')


print(sum('1', 2))
 """
