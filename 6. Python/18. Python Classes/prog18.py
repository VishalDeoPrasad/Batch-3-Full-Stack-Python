from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def show(self):
        pass

class Student(Person):
    def __init__(self):
        self.name = "Vishal Kumar"

    def show(self):
        print("Name:", self.name)

s = Student()
s.show()
