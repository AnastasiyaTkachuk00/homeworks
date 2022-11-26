import random

mylist = []
for i in (range(0, 10)):
    mylist.append(random.randint(-100, 101))
print(mylist)

mylist[2] = random.choice(mylist)
print(mylist)
