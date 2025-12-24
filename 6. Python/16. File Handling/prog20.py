try:
    file = open("demo9.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File Not found!")