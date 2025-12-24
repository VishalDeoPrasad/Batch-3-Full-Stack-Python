import os

if os.path.exists("demo.text"):
    os.rename("demo.text", "sample1.txt")
else:
    print("File not found!")