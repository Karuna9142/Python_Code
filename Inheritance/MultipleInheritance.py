class Calculation:
    def sum(self,a,b):
        return a+b

class Calculation1:
    def __mul__(self, a,b):
        return a*b

class Derive(Calculation,Calculation1):
    def devide(self, a,b):
        return a/b


d = Derive()
print(d.sum(10,20))
print(d.__mul__(5,6))
print(d.devide(20,10))




