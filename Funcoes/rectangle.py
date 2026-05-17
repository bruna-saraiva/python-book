def rectangle(width, height, character="*"):
    line = character * width
    for i in range(height):
        print(line)

rectangle(width=9, height=3)