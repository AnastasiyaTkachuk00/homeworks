import random 
from random import randint


AVAILABLE_NAMES = ('John', 'Jane', 'Mary', 'David', 'Alex', 'Max', 'Nick', 'Anastasia', 'Leo')
AVAILABLE_COLORS = ('blue', 'green', 'brown', 'grey', 'black')
nickname_digits = [1, 2, 3, 4, 5]


class User:
    def __init__(self, name, nickname, age, eye_color):
        
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eye_color = eye_color
        

    @property
    def info(self):
        dict = {'Name': self.name, 'Nickname': self.nickname, 'Age': self.age, 'Eye_color': self.eye_color}
        return dict
        
    def __eq__(self, age):
        return self.age == user.age and self.age == user.age

    def __gt__(self, age):
        return user.age > user.age

    def __ge__(self, age): 
        return user.age >= user.age


def users_generator(number):
    name = random.choice(AVAILABLE_NAMES)
    for i in range(0, 50):
       user = User( name,
       nickname = (name, random.sample(nickname_digits, 5)),
       age = random.randint(0, 100),
       eye_color = random.choice(AVAILABLE_COLORS))
    yield user  
    
       
gen = users_generator(50)
for user in gen:
    print(user.info)
