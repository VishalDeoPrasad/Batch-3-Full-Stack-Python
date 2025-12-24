lst = [10,5,3,5,7]

try:
    print(lst[40])
except IndexError:
    print("Index out of range!")

