with open("demo.txt", "r") as file:
    print(file.tell())
    print(file.read(50))
    print(file.tell())