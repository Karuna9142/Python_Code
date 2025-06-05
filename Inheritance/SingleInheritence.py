# class Animal:
#     name = "Priya"
#
#     def eat(self):
#         print("I wanna eat something")
#
# class Dog(Animal):
#
#     def display(self):
#         print("My name is - ", self.name)
#
# d = Dog()
# d.name = "Munu"
# #d.name
# d.eat()
# d.display()



class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()
obj.bark()
obj.speak()