"""
proper way to open a file
automatic close the file
write to a file
'r'	Reads from a file and returns an error if the file does not exist (default).
'w'	Writes to a file and creates the file if it does not exist or overwrites an existing file.
'x'	Exclusive creation that fails if the file already exists.
'a'	Appends to a file and creates the file if it does not exist or overwrites an existing file.
'b'	Binary mode. Use this mode for non-textual files, such as images.
't'	Text mode. Use only for textual files (default).
'+'	Activates read and write methods.
"""
try:
    with open('sad.txt', mode='r') as my_file:
        text = my_file.readlines()
        print(text)
except FileNotFoundError as err:
    print('File does not exist!')

# pathlib is a useful lib to set a path t a file in different OS
