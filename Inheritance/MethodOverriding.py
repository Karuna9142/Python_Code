class Car:
   brand = "Fortuner"

   def drive(self):
       print("I want to drive a car")

class Honda(Car):
    def drive(self):
        print("My car name is - ", self.brand)
        print("This is my Car")


h1 = Honda()
#without super we cant call the  method of class car
h1.drive()
h1.brand