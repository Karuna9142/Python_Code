#List
#mutable
l = [2,3,4,5,6]
l[0] = 9
print(l,type(l))

#tuple
#immutable

t = (3,4,5,6,7)

print(t, type(t))
print(len(t))
print(t[3])
print(t[2:4])
print(t[2:])

t1 = ('apple','banana','cherry')
if 'apple' in t1:
    print("Yes")

# we can change the value of tuple by changing it into list
t3 = list(t)
t3[0] = 'kiwi'
t = tuple(t3)

print(t)

x = {'a','b','c','d'}
y = list(x)
y.append('e')

x = tuple(y)
print(x)