import os

try:
    if os.path.exists("new"):
        os.rmdir("new")
except PermissionError:
    print("You do not have permission to access this file")
