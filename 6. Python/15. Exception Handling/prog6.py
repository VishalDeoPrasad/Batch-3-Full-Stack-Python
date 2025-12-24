try:
    open("abc.txt", "r")
except FileNotFoundError:
    print("Check your file name!")