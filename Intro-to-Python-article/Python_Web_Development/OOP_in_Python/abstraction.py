from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(f"{self.name} is starting the engine.")

    def stop(self):
        print(f"{self.name} is stopping the engine.")

class Motorcycle(Vehicle):
    def start(self):
        print(f"{self.name} is starting the engine.")

    def stop(self):
        print(f"{self.name} is stopping the engine.")

car = Car("Toyota")
car.start()
car.stop()

motorcycle = Motorcycle("Harley Davidson")
motorcycle.start()
motorcycle.stop()
