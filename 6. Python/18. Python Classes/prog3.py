class Addition:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print(self.n1 + self.n2)
    
    def sub(self):
        print(self.n1 - self.n2)

    def multi(self):
        print(self.n1 * self.n2)

    def div(self):
        print(self.n1 / self.n2)

a = Addition(10,20)
a.add()
a.sub()
a.multi()
a.div()


