MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 100,
    "coffee": 100,
}
profit = 0


def report():
    """Prints a report of available resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(order):
    """Check if there are enough resources for the order."""
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if item not in resources:
            return False
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(order):
    """Deduct the required ingredients from resources."""
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order}, Enjoy it!")


def calculate_money(pennies, nickels, dimes, quarters):
    """Calculate the total value of coins inserted."""
    total_cents = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)
    return total_cents / 100


def main():
    global profit

    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "report":
            report()
        elif order == "off":
            break
        elif order in MENU:
            if check_resources(order):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                user_funds = calculate_money(pennies, nickels, dimes, quarters)
                order_cost = MENU[order]["cost"]

                if user_funds < order_cost:
                    print("Sorry, you don't have enough money. Money refunded.")
                else:
                    profit += order_cost
                    change = user_funds - order_cost
                    if change > 0:
                        print(f"Here is your change: ${round(change, 2)}")
                    make_coffee(order)
            else:
                pass
        else:
            print("Unknown choice. Please try again.")


if __name__ == "__main__":
    main()
