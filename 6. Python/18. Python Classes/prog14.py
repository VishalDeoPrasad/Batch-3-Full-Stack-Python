class A:
    def alpha(self):
        print("Hi, I'm in class A")

class B(A):
    def alpha(self):
        print("HI, I'm in class B")
b = B()
b.alpha()