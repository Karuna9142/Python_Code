#return a number between 5 and 10

import random
print(random.randint(5,10))

#return a number between 3(included)and 9(not included)
print(random.randrange(3,9))

# choice() method
# l = ["apple","banana", "cherry"]
# print(random.choice(l))

#random() - return a random float between 0 and 1
# r = random.random()
# print(r)

l = [10,20,30,40]
random.shuffle(l)
print(l)

u = random.uniform(3,9)
print(u)
