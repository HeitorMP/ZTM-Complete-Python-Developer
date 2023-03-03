
# Hight Order Function HOC (accept or return other function)
# ex: reduce
'''
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func

'''

# Decorator Pattern (passing many arguments as we want)


from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


@my_decorator
def hello(greeting, emoji, haha):
    print(greeting, emoji, haha)


hello('hello', ':p', 'haha')


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print('took {} ms'.format(t2-t1))
        return result
    return (wrapper)


@performance
def long_time():
    for i in range(100000000):
        i * 5


@performance
def hello():
    print('lala')
    print('lala')
    print('lala')
    print('lala')


long_time()

hello()
