class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Vishal Kumar", 101)
s2 = Student("Amit Kumar", 102)
s1.show()
s2.show()



        
