try:
    num = int(input("Enter a number:"))
    ans = 10/num
    print(ans)
except ValueError:
    print("Please enter only digit!")
except ZeroDivisionError:
    print("Don't enter zero")