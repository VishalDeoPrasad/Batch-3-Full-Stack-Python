class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)
    
s1 = Student("Vishal", ['Maths', 'C', 'C++'])
print(len(s1))