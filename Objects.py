class Car:
    def __init__(self):                     # ########################## Constructor # #############################
        self.carLength = 250
        self.__carWidth = 120
        self.__wheels = 4                   # ########################## Encapsulation __name # #############################
        self.readyToStartBoolean = False
        self.riding = False

    def startRiding(self, gas, oil, doors):
        if not self.riding:
            self.__checkCarStatus(gas, oil, doors)
        
        if self.riding:
            print("The car is already on")
        elif self.readyToStartBoolean:
            self.riding = True
            print("The car turned on")
        else:
            print("The car is not OK to START")
            self.riding = False

    def __checkCarStatus(self, gas, oil, doors):
        print("Checking status: ")

        self.gas = gas
        self.oil = oil
        self.doors = doors

        self.__readyToStart()

    def __readyToStart(self):

        if self.gas.upper() == "OK" and self.oil.upper() == "OK" and self.doors.upper() == "CLOSED":
            self.readyToStartBoolean = True
        else:
            self.readyToStartBoolean = False

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


myCar = Car()
print("The length is: ", myCar.carLength)
print("The car is on? ", myCar.riding)
myCar.startRiding("OK", "not OK", "Closed")
print("-------------------------------------")
myCar2 = Car()
myCar2.startRiding("OK", "ok", "Closed")
myCar2.startRiding("OK", "ok", "Closed")

print(myCar)
print(myCar2)
