#Setters and Getters

class Student:
    def __init__(self):
        self.name = "Vishal Kumar"
        self.__marks = 98

    def get_marks(self):
        return self.__marks
    
    def set_marks(self, value):
        self.__marks = value

s1 = Student()
print(s1.name)
print(s1.get_marks())

s1.set_marks(99)
print(s1.get_marks())
