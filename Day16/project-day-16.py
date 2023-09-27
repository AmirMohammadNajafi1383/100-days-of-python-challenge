class CoffeeMachine:
    def __init__(self):
        self.MENU = {
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
        self.resources = {
            "water": 300,
            "milk": 100,
            "coffee": 100,
        }
        self.profit = 0

    def report(self):
        """Prints a report of available resources and profit."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.profit}")


    def check_resources(self , order):
        """Check if there are enough resources for the order."""
        ingredients = self.MENU[order]["ingredients"]
        for item in ingredients:
            if item not in self.resources:
                return False
            if ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True
    
    def make_coffee(self, order):
        """Deduct the required ingredients from resources."""
        ingredients = self.MENU[order]["ingredients"]
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"Here is your {order}, Enjoy it!")

    def calculate_money(self, pennies, nickels, dimes, quarters): 
        """Calculate the total value of coins inserted."""
        total_cents = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)
        return total_cents / 100
    
    def main(self):
        while True:
            order = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if order == "report":
                self.report()
            elif order == "off":
                break
            elif order in self.MENU:
                if self.check_resources(order):
                    print("Please insert coins.")
                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickels = int(input("How many nickels?: "))
                    pennies = int(input("How many pennies?: "))
                    user_funds = self.calculate_money(pennies, nickels, dimes, quarters)
                    order_cost = self.MENU[order]["cost"]

                    if user_funds < order_cost:
                        print("Sorry, you don't have enough money. Money refunded.")
                    else:
                        self.profit += order_cost
                        change = user_funds - order_cost
                        if change > 0:
                            print(f"Here is your change: ${round(change, 2)}")
                        self.make_coffee(order)
                else:
                    pass
            else:
                print("Unknown choice. Please try again.")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.main()