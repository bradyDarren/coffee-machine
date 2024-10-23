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
    if coin_total >= recipes[coffee_selection]["cost"]: 
        change = coin_total - recipes[coffee_selection]["cost"]
        return f"You ordered a {coffee_selection} for a total price of {change}." 
    else: 
        return f"Please enter {change} more to purchase your selected item."


# def order(): 
#     user_choice = input("What would you like to order? (expresso/latte/cappuccino)")



