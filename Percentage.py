marks = int(input("Enter the marks?"))

if marks>85 and marks<=100:
    print("Congrats! you scored grade A")
elif marks>60 and marks<=85:
    print("Grade B")
elif marks > 45 and marks <= 60:
    print("Grade C")
else:
    print("Fail")

