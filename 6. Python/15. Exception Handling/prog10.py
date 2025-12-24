class NegAgeError(Exception):
    pass

age = int(input("Enter Your Age:"))
if age < 0:
    raise NegAgeError("Age Must be Positive!")
print(age)