class Animal:
    name = ""

    def eat(self):
        print('I can not eat')

# inherit from Animal
class Dog(Animal):

    def eat(self):
        super().eat()
        print('my friends can eat')

d = Dog()
d.eat()