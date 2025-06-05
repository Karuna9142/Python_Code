l = [10,20,30,40,50,60]
t = len(l)

# for n in range(t):
#     print(l[n],end=' ')

for a in l:
    print(a, end= ' ')

print("\nList in reverse order")
for x in range(t-1, -1, -1):
    print(x, end=' ')