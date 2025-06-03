import random
cnum = random.randrange(1, 101)
n = int(input("Enter your number:- ---"))

if n>cnum:
    print("Computer number", cnum)
    print("Your guess number is too high")
elif cnum>n:
    print("Computer number", cnum)
    print("your guess number is too low")
else:
    print("Computer number", cnum)
    print("Your guess number is correct")