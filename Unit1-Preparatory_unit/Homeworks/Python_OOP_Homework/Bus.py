class Vehicule():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicule):
    pass
        
Etuza = Bus(200, 300)
print("The Etuza bus has max speed of", Etuza.max_speed," Km/h and a mileage of", Etuza.mileage, " Miles.")