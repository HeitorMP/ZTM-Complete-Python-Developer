import re

pattern = re.compile(r"(^[a-zA-Z\d_.+-]+@[a-zA-Z\d-]+\.[a-zA-Z0-9-.]+$)")

string = 'Andrei@lala'

a = pattern.search(string)
print(a)

"""
Exercise password validation
at least 8 char long
contain ane sort letters, numbers $%#@
has to end with a number
"""

password_pattern = re.compile(r"([a-zA-Z0-9$%#@]){7,}[0-9]")
password = input('type your password: ')
print(password)

valid_pass = password_pattern.fullmatch(password)
print(valid_pass)
