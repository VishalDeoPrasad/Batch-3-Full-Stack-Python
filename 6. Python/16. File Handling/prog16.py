import os

if os.path.exists("demo3.txt"):
    with open("demo3.txt", "r") as file:
        print(file.read())
else:
    print("file not found!")