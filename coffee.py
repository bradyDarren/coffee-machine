from data import recipes, money, resources
from art import logo

def coin_calc(qcount, dcount, ncount, pcount):
# takes coin qauntity and returns the sum of all the coins.
    qsum = qcount * money["quarter"]
    dsum = dcount * money["dime"]
    nsum = ncount * money["nickle"]
    psum = pcount * money["penny"]
    total = psum + nsum + dsum + qsum
    return total

# test line
# print(coin_calc(5,3, 5,1))

def transaction_cost(coin_total, coffee_selection):
    cost = recipes[coffee_selection]["cost"]
    if coin_total >= cost: 
        change = coin_total - cost
        resources["money"] += cost
        return f"You ordered a {coffee_selection} for a total price of ${cost}, your change is ${change}." 
    else:
        change = coin_total - cost 
        return f"Sorry amount inserted is not enough money. Please enter ${abs(change)} more to purchase your selected item."

for key in recipes['latte']:
    print(key)

# def transaction_ingredients(user_selection):
#     if user_selection == "report":
#         return resources
#     else:
#         ingredients_used = recipes[user_selection]
#         for key in ingredients_used:
#             if key in resources:
                
#         return resources

# machine_on = True

# def order():
#     while machine_on: 
#         user_choice = input("What would you like to order? (expresso/latte/cappuccino)").lower()
#         if resources





