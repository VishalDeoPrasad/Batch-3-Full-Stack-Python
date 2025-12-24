class Company:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def show(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:", self.dept)

emp1 = Company("Vishal", "2LPM", "IT")
emp2 = Company("Neha", "1LPM", "HR" )
emp3 = Company("Priya", "1.5LPM", "Finance")

emp1.show()
emp2.show()
emp3.show()

    