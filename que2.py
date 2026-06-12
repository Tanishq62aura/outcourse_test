from abc import ABC, abstractmethod
class vehicle:
    def start(self):
        pass
    def stop(self):
        pass
    def fuel_type(self):
        pass

class car(vehicle):
    def start(self):
        print("Car starts")
    def stop(self):
        print("car stopped")
    def fuel_type(self):
        print("petrol")

class bike(vehicle):
    def start(self):
        print("bike starts")
    def stop(self):
        print("bike stopped")
    def fuel_type(self):
        print("petrol")

class Tesla(vehicle):
    def start(self):
        print("Tesla starts")
    def stop(self):
        print("Tesla stopped")
    def fuel_type(self):
        print("Electric")

c = car()
c.start()
c.stop()
c.fuel_type()


b = bike()
b.start()
b.stop()
b.fuel_type()


t = Tesla()
t.start()
t.stop()
t.fuel_type()
