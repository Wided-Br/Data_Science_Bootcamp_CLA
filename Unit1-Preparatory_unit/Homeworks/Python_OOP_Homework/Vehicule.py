class Vehicule():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

speed = int(input("Enter the car's speed: "))
mile = int(input("Enter the car's mileage: "))
car = Vehicule(speed, mile)
print("The car's speed is ",car.max_speed, " Km/h, and it can travel ", car.mileage , " Miles.")
