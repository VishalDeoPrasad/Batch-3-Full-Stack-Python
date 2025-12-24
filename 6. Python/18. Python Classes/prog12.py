class Person:
    def __init__(self):
        self.name = "Vishal Kumar"

class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll = 101

    def show(self):
        print("Name:", self.name)
        print("Roll no:", self.roll)

s = Student()
s.show()





