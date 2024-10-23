from data import recipes, money, resources
from art import logo

def coin_input(qcount, dcount, ncount, pcount):
    qsum = qcount * money["quarter"]
    print(qsum)

coin_input()