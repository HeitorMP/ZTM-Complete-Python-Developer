
# Under the hood for
def special_for(iterable):
    iterable = iter(iterable)
    while True:
        try:
            print(next(iterable))
        except StopIteration:
            break


# Under the hood range
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


special_for([1, 2, 3])
gen = MyGen(0, 100)

for n in gen:
    print(n)
