class Vehicle:
    def start(self):
        print("Vehicle Start")

class Car(Vehicle):
    def drive(self):
        print("Car Drives")

class ElectricCar(Car):
    def charge(self):
        print("Car Charging...")

e = ElectricCar()
e.start()
e.charge()
e.drive()