
my_file = open('test.txt')

print(my_file.read())  # read and cursor goes to the end of file
my_file.seek(0)  # move the cursor to the position 0
print(my_file.read())
my_file.seek(0)

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)

print(my_file.readlines())  # list of lines

my_file.close()
