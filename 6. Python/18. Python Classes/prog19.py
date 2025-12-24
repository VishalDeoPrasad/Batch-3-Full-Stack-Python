from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Starts")

    def stop(self):
        print("Car Stops:")

c = Car()
c.start()
c.stop()

    
