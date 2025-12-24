class Animal:
    def sound(self):
        print("Animal makes a sound!")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Makes a sound!")

d = Dog()
d.sound()
