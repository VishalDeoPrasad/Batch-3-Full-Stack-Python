bill = int(input("Enter Your Bill Amount:"))

if bill >= 2000:
    print("You Got 20% Discount")
elif bill >= 1500:
    print("You got 15% Discount")
elif bill >= 1000:
    print("You got 10% Discount")
elif bill >= 500:
    print("You got 5% Discount")
else:
    print("No Discount for you")