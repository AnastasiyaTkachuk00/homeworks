import random

mylist = []
for i in range(10):
    mylist.append(random.randint(-100, 101))
print(mylist)

mylist[2] = random.choice(mylist)
del mylist[6]
print(mylist)
