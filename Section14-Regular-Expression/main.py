import re

string = 'heitor maciel Pinto'
"""
pattern = re.compile('search inside of this text please! this')

a = pattern.search(string)
print(a.span())  # where 'this' occurs
print(a.start())  # where 'this' start
print(a.end())
print(a.group())

b = pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)

d = pattern.match(string)
print(d)
"""
pattern2 = re.compile(r"([a-zA-Z]).([P])")  # r = raw string, ignore any python special char like \ \n \t etc
v = pattern2.search(string)
print(v.span())
v = pattern2.findall(string)
print(v)