#Public vs Private Variable

class Student:
    def __init__(self):
        self.name = "Vishal Kumar"
        self.__marks = 98

s1 = Student()
print(s1.name)
print(s1._Student__marks) #not a good way to access private variable