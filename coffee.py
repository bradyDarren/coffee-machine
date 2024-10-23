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

# def report(): 


def process_order(coin_total, coffee_selection):
    cost = recipes[coffee_selection]["cost"]
    if coin_total >= cost: 
        change = coin_total - cost
        return f"You ordered a {coffee_selection} for a total price of ${cost}, your change is ${change}." 
    else:
        change = coin_total - cost 
        return f"Please enter ${abs(change)} more to purchase your selected item."

print(process_order(3.00,"latte"))


# def order(): 
#     user_choice = input("What would you like to order? (expresso/latte/cappuccino)")



