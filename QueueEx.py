l = []
while True :
    c = int(input('''
      1. Push Element
      2. Pop  First Element
      3. Front Element
      4. Last  Elements
      5. Display Stack
      6. Exit
    '''))
    if c == 1:
        n = input("Enter the value")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("queue is empty")
        else:
            del l[0]
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("queue is empty")
        else:
            print("First Queuw Element " ,l[0])

    elif c == 4:
        if len(l) == 0:
            print("queue is empty")
        else:
            print("First Queuw Element ", l[-1])
    elif c == 5:
        print("Display queue", l)

    elif c == 6:
        break
    else:
        print("Invalid Operation")
