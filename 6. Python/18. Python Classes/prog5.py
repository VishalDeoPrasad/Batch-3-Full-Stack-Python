class Student:
    school = "Manac infotech"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Vishal Kumar", 99)
s2 = Student("Rahul Kumar", 95)
s2.show()
print(s2.school)

