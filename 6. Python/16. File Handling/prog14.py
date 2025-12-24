with open("demo.txt", "r") as file:
    print(file.tell())
    file.seek(15)
    print(file.read())