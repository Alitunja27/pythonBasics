class Car:
    def riding(self):
        print("I'm moving using my 4 wheels")


class Bike:
    def riding(self):
        print("I'm moving using 2 wheels")


class Truck:
    def riding(self):
        print("I'm moving using 16 wheels")


def drivingVehicle(vehicle):
    vehicle.riding()


myTruck = Truck()
drivingVehicle(myTruck)
