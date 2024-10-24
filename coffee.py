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
a = coin_calc(5,3, 5,1)
print(a)

def transaction_cost(coin_total, coffee_selection):
    cost = recipes[coffee_selection]["cost"]
    if coin_total >= cost: 
        change = coin_total - cost
        resources["money"] += cost
        return f"You ordered a {coffee_selection} for a total price of ${cost}, your change is ${round(change),2}." 
    else:
        change = coin_total - cost 
        return f"Sorry amount inserted is not enough money. Please enter ${(abs(change))} more to purchase your selected item."

# test line
b = transaction_cost(a,"latte")
print(b)

def transaction_ingredients(user_selection):
    if user_selection == "report":
        return resources
    else:
        ingredients_used = recipes[user_selection]
        for key in ingredients_used:
            if key in resources:
                order_ingredient = ingredients_used[key]
                machine_resource = resources[key]
                if order_ingredient <= machine_resource:
                    resources[key] = resources[key] - ingredients_used[key]
            if order_ingredient > machine_resource: 
                return f"Machine doesn't have enough {key} to fullfill the selected order."
        return resources
    
# test line
c = transaction_ingredients("latte")
print(c)

def order():
    machine_on = True
    while machine_on: 
        user_choice = input("What would you like to order? (expresso/latte/cappuccino): ").lower()
        if user_choice == 'off':
            print("Coffee Machine is now turned off.")
            machine_on = False
        elif user_choice in recipes:
            order_ingredients = transaction_ingredients(user_choice)
            print(order_ingredients)
            quarters_input = int(input("How many quarters would you like to input?: "))
            dimes_input = int(input("How many dimes would you like to input?: "))
            nickles_input = int(input("How many nickles would you like to input?: "))
            pennies_input = int(input("How many pennies would you like to input?: "))
            user_money = coin_calc(quarters_input, dimes_input, nickles_input, pennies_input)
            order_cost = transaction_cost(user_money, user_choice)
            return order_cost
        
print(order())




