from data import recipes, money, resources
from art import logo

def coin_calc(qcount, dcount, ncount, pcount):
    qsum = qcount * money["quarter"]
    dsum = dcount * money["dime"]
    nsum = ncount * money["nickle"]
    psum = pcount * money["penny"]
    total = psum + nsum + dsum + qsum
    return total

print(coin_calc(5,3, 5,1))

def report(): 


def process_order(coin_total, coffee_selection):
    


