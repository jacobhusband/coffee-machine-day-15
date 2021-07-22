MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def add_resource(a):
    print(f"Adding 300ml of {a}")
    resources[a] += 300


def check_resources(t):
    for i in t["ingredients"]:
        if t["ingredients"][str(i)] > resources[str(i)]:
            print(f"Not sufficient {i}!")
            ans = input(f"Want to ask if they can add that resource {i}? (yes/no) ")
            if ans == "yes":
                return add_resource(i)
            else:
                return print("Have a nice day!")
        else:
            return add_coins(t)


def add_coins(c):
    print("We only accept coins here.")
    q = int(input("Quarters: "))
    d = int(input("Dimes: "))
    n = int(input("Nickels: "))
    p = int(input("Pennies: "))
    cash = ((q*25) + (d*10) + (n*5) + p)/100
    cost = c["cost"]
    if cost > cash:
        print(f"Total cash: ${cash:.2f}")
        print(f"Cost of drink: ${cost:.2f}")
        return print("Sorry, insufficient funds, money refunded.")
    elif cost <= cash:
        change = cash - c["cost"]
        change = round(change, 2)
        print(f"Total cash: ${cash:.2f}")
        print(f"Cost of drink: ${cost:.2f}")
        print(f"Change: ${change:.2f}")
        update_resources(c)
        return print("Enjoy your coffee!")
    else:
        print("Sorry, try again")
        return add_coins(c)


def update_resources(r):
    resources["water"] -= r["ingredients"]["water"]
    if "milk" in r["ingredients"]:
        resources["milk"] -= r["ingredients"]["milk"]
    resources["coffee"] -= r["ingredients"]["coffee"]
    resources["money"] += r["cost"]


def check_name(c):
    if c == 'espresso':
        t = MENU["espresso"]
        check_resources(t)
    elif c == 'latte':
        t = MENU["latte"]
        check_resources(t)
    elif c == 'cappuccino':
        t = MENU["cappuccino"]
        check_resources(t)
    elif c == 'off':
        return print("Have a good day!")
    elif c == 'report':
        return report()
    else:
        return print("Sorry, what was that?")


def report():
    w = resources["water"]
    m = resources["milk"]
    c = resources["coffee"]
    mo = resources["money"]

    return print(f"""Water: {w}ml
Milk: {m}ml
Coffee: {c}ml
Money: ${mo} """)


if __name__ == '__main__':
    coffee = ''
    while coffee != "off":
        coffee = input('What would you like to drink? (espresso/latte/cappuccino) ')
        check_name(coffee)
