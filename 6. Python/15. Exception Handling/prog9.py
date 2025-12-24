try:
    num = int(input("Enter a number:"))
    ans = 10/num
except (ValueError, ZeroDivisionError):
    print("Some Error Occurred!")
except Exception:
    print("Some more error occurred!")
else:
    print(ans)
finally:
    print("I will run always!")
