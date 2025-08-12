# 2 player dice game using function

import random

def player():
    initial = random.randint(1,6)
    print(initial)
    sum = 0
    for i in range(initial):
        b = random.randint(1,6)
        sum += b
        return sum
p1 = player()
p2 = player()

if p1 > p2:
    print('Player1 wins')
else:
    print('Player2 wins')