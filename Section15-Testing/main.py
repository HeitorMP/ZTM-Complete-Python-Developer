def do_stuff(num=0):
    try:
        return int(num) + 5 if num else 'please enter number'
    except ValueError as err:
        return err

