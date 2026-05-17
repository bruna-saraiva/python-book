names = ["Ana", "Carlos", "Maria"]

# using oficial exception errors
# for trial in range(3):
#     try:
#         i = int(input("dial the index from the name you want to print: "))
#         print(names[i])
#     except ValueError:
#         print("dial a number, not a character")

#     except IndexError:
#         print("invalid value, dial between -3 and 3")

# using customized exceptions
for trial in range(3):
    try: 
        i = int(input("dial the index from the name you want to print: "))
        print(names[i])
    except Exception as e:
        print(f"something wrong happened: {e}")

