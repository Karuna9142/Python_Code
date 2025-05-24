l = []
while True :
    c = int(input('''
      1. Push Element
      2. Pop Element
      3. Peek Element
      4. Display Stack
      5. Exit
    '''))
    if c == 1:
        n = input("Enter the value")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Stack is empty")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Stack is empty")
        else:
            print("Last Element " ,l[-1])
    elif c == 4:
        print("Display stack", l)

    elif c == 5:
        break
    else:
        print("Invalid Operation")













# l = []
# while True :
#     c = int(input('''
#        1 Push Elements
#        2 Pop Elements
#        3 Peek Elements
#        4 Display Stack
#        5 Exit
#     '''))
#     if c==1:
#         n = input("Enter the value - ")
#         l.append(n)
#         print(l)
#     elif c == 2:
#         if len(l) == 0:
#             print("Empty Stack")
#         else:
#             p = l.pop()
#             print(p)
#     elif c == 3:
#         if len(l) == 0:
#             print("Empty Stack")
#         else:
#             print("Last stack Element",l[-1])
#     elif c == 4:
#         print("Display stack", l)
#     elif c == 5:
#         break