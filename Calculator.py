a = int(input("Enter first number:-"))
b = int(input("Enter first number:- "))

opr = input("Enter the operator:- ")
if opr=='+':
    print(a+b)
elif opr =='-':
    print(a-b)
elif opr=='*':
    print(a*b)
elif opr=='/':
    print(a/b)
elif opr=='%':
    print(a%b)
else:
    print("Invalid Input")

