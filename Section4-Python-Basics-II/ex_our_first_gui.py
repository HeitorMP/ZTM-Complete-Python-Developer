# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'.
# This will reveal an image!

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for line in picture:
    for col in line:
        if col == 0:
            print(' ', end='')
        elif col == 1:
            print('*', end='')
    print()

# Cleaner code sugested by teacher
# Same
