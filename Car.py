# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it is called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.



# Car class

speed = 0

accelerate = speed + 5

brake = speed - 5

class Car:
    def __init__(self, make, model, year, speed, accelerate, brake):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0
        self.__accelerate = speed + 5
        self.__brake = speed - 5

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_speed(self, speed):
        self.__speed = 0

    def set_acceleration(self, accelerate):
        self.__accelerate = speed + 5

    def set_brake(self, brake):
        self.__brake = speed - 5

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def get_acceleration(self):
        return self.__accelerate

    def get_brake(self):
        return self.__brake
