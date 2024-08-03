class Car:
    company="Mahindra"
    Model = "CAR10415B25"
    Name = "Scorpio"

    def __init__(self):
        print("Constructer is called")
        self.key = False
        self.cluch = False
        self.brk = False
        self.acc = False

    def start(self):
        self.key = True
        self.cluch = True
        self.acc = True
        print("Car started")

    def stop(self):
        self.key = False
        self.brk = True
        self.acc = False
        print("Car is stopped")

c1 = Car()
# Car.start() # produce an error becouse missing 1 required positional argument: 'self'
# Car.start(c1) # Not produce any error becouse missing 1 required positional argument: 'self' was given as object self
c1.start() #shorthand to call class function
print(f"key: {c1.key}\n cluch: {c1.cluch}\naccelerater: {c1.acc}")
print("\n")
c1.stop()
print(f"key: {c1.key}\nbreak: {c1.brk}\naccelerater: {c1.acc}")
print(c1.__sizeof__())



        