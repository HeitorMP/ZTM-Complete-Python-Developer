def get_myfile(argv):
    try:
        file_path = argv[1]
    except IndexError:
        file_path = "test.txt"

    try:
        with open(file_path, 'r') as my_file:
            text = my_file.read()
    except (FileNotFoundError, NameError) as err:
        try:
            with open("test.txt", mode='w+') as my_file:
                my_file.write('this file was created because your file was not found!')
                text = my_file.read()
        except IOError as err:
            return None
    return text


def no_permission_routine():
    print('File could not been created!\nCheck your permission!')
    exit(1)
