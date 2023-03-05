
# built in modules
import sys
from random import randrange


def get_value(argv):
    """ checks if the values ​​passed as a parameter are valid numbers, otherwise it returns a default value. [0,10]
    Args:
        argv (list): sys.argv content
    Returns:
        list: list with 2 values to be used as range!
    """
    values = []
    try:
        100
        values.append(int(argv[1]))
        values.append(int(argv[2]))
    except (ValueError, IndexError):
        print('Some of values are invalid, using the standard range!')
        return [0, 10]

    if values[0] >= values[1]:
        print('impossible to make a range with these two values!')
        print('Using the standard range!')
        return [0, 10]

    return values


def is_guess_correct(guess, answer):
    """ check if the player guessed the answer
    Args:
        guess (int): player guess
        answer (int): expected answer
    Returns:
        bool: True if guess == answer otherwise it returns false
    """
    if guess == answer:
        return True
    elif guess < answer:
        print('Guess higher')
    else:
        print('Guess lower')
    return False


range_li = get_value(sys.argv)
answer = randrange(range_li[0], range_li[1])
guess = answer + 1  # to make sure that guess will never start == answer
attempts = 1
print('Type q to quit!')
while True:
    guess = input(
        f'Try guess a number between {range_li[0]} - {range_li[1]}: ')
    if guess == 'q':
        break
    try:
        guess = int(guess)
    except:
        print('Invalid value, try again!')
        continue
    if is_guess_correct(guess, answer):
        print(f'congratulations you guessed it with {attempts} tries ')
        break
    attempts += 1

print('Good bye and thanks for playing!')

# official sollution
'''
from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue
'''
