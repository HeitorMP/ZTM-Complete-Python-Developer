# Print a formated string the show user_name and password as *

user_name = input('Username: ')
password = input('Password: ')

print("{0}, your password {1} is {2} letters long!".format(
    user_name, '*' * len(password), len(password)))
