class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def cute(self):
        print("Puppies are cute")

p = Puppy()
p.speak()
p.bark()
p.cute()

print("*****************")
d = Dog()
d.bark()
d.speak()