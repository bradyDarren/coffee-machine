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

# # test line
# a = coin_calc(5,3, 5,1)
# print(a)

def transaction_cost(coin_total, coffee_selection):
# evaluates if the user desired selection and the sum of the coin input. 
    cost = recipes[coffee_selection]["cost"]
    if coin_total >= cost: 
        change = coin_total - cost
        resources["money"] += cost
        return f"You ordered a {coffee_selection} for a total price of ${cost}, your change is ${round(change,2)}." 
    else:
        change = coin_total - cost 
        return f"Sorry amount inserted is not enough money. Please enter ${(abs(change))} more to purchase your selected item."

# # test line
# b = transaction_cost(a,"latte")
# print(b)

def transaction_ingredients(user_selection):
# evaluates if there are enough resources to fill the users desired order.
    ingredients_used = recipes[user_selection]
    for key in ingredients_used:
        if key in resources:
            order_ingredient = ingredients_used[key]
            machine_resource = resources[key]
            if order_ingredient <= machine_resource:
                resources[key] -= ingredients_used[key]
            if order_ingredient > machine_resource: 
                return f"Machine doesn't have enough {key} to fullfill the selected order."
# test line
# c = transaction_ingredients("latte")    
# print(c)

def check_num(prompt):
# confirms if entered number is an integer.
    while True: 
        try:
            return int(input(prompt))
        except ValueError: 
            print("Invalid input. Please input a number")
    

def order():
    machine_on = True
    while machine_on: 
        user_choice = input("What would you like to order? (expresso/latte/cappuccino): ").lower().strip()
        if user_choice == 'off':
            print("Coffee Machine is now turned off.")
            machine_on = False
        elif user_choice == "report":
            for key, value in resources.items():
                print(f"{key} : {value}")
            continue
        elif user_choice not in recipes:
            print("Invalid Input. Please input a given choice.")
            continue
        elif user_choice in recipes:
            ingredients_check = transaction_ingredients(user_choice)
            if isinstance(ingredients_check,str):
                print(ingredients_check)
                continue

        quarters_input = check_num("How many quarters would you like to input?: ")
        dimes_input = check_num("How many dimes would you like to input?: ")
        nickles_input = check_num("How many nickles would you like to input?: ")
        pennies_input = check_num("How many pennies would you like to input?: ")
        user_money = coin_calc(quarters_input, dimes_input, nickles_input, pennies_input)
        order_cost = transaction_cost(user_money, user_choice)
        print(order_cost)
print(order())




