


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"The {self.name} makes a {self.sound} sound.")

class Bird(Animal):
    def __init__(self, name, sound, flight_altitude: int):
        super().__init__(name, sound)
        self.flight_altitude = self.validate_flight_altitude(flight_altitude)
    @staticmethod
    def validate_flight_altitude(flight_altitude):
        if type(flight_altitude) != int:
            raise 'flight_altitude must be int'
        if flight_altitude <= 0:
            raise 'flight_altitude cannot be zero'
        return flight_altitude
    def set_flight_altitude(self, flight_altitude):
        self.flight_altitude = self.validate_flight_altitude(flight_altitude)


    def fly(self):
        print(f"The {self.name} is flying at an altitude of {self.flight_altitude} meters.")


lion = Animal("lion", "roar")
parrot = Bird("parrot", "squawk", 100)
lion.make_sound()  
parrot.make_sound()  
parrot.fly() 
