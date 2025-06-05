class Bank:
    def roi(self):
        return 10

class Sbi(Bank):
    def roi(self):
        return 7

class ICICI(Bank):
    def roi(self):
        return 8

b1 = Bank()
b2 = Sbi()
b3 = ICICI()

print("Bank rate of interest:",b1.roi())
print("SBI rate of interest:",b2.roi())
print("ICICI rate of interest:",b3.roi())

