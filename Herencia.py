class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.driving = False
        self.accelerate = False
        self.breaking = False

    def turnOn(self):
        self.driving = True

    def acelerate(self):
        self.accelerate = True

    def breakingTheVehicle(self):
        self.breaking = True

    def status(self):
        print("Brand: ", self.brand, "\nModel: ", self.model, "\nDriving: ", self.driving, "\nAccelerating",
              self.accelerate, "\nBreaking: ", self.breaking)

class Furgo(Vehicle):
    def haul(self, haul):
        self.hauled = haul
        if self.hauled:
            return "The furgo is loaded"
        else:
            return "The furgo is not loaded"


class Bike(Vehicle):
    hCaballito = ""

    def caballito(self):
        self.hCaballito = "I'm riding my bike doing the Caballito"

    def status(self):
        super().status()
        print(self.hCaballito)


class ElectricVehicles:
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.autonomy = 100

    def charging(self):
        self.charging = True


myBike = Bike("Honda", "CBR")
myBike.caballito()
myBike.status()
print("-----------------------------------------")
myFurgo = Furgo("Chevrolet", "Cualquiera")
myFurgo.acelerate()
myFurgo.status()
print(myFurgo.haul(True))


class ElectricBicycle(ElectricVehicles, Vehicle):
    pass


print("------------------------------------")
myBicycle = ElectricBicycle("Shimano", "TRD")
myBicycle.status()
print(isinstance(myBicycle, ElectricBicycle))


