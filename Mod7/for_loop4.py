# Print only integers

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color_loop in colors:
    if isinstance(color_loop, int):
        print(color_loop)
