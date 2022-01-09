from assets import MENU, resources, logo
from os import system, name


class CoffeeMachine():
    __money = 0

    def __clear_console(self):
        return system('cls') if name in ['nt', 'dos'] else system('clear')

    def collect_money(self, cost) -> bool:
        while True:
            try:
                ten = 10 * int(input("How many ₹10 note? "))
                twenty = 20 * int(input("How many ₹20 note? "))
                fifty = 50 * int(input("How many ₹50 note? "))
                hundred = 100 * int(input("How many ₹100 note? "))
            except ValueError:
                print("Please provide a valid input!")
                continue
            break

        total = ten + twenty + fifty + hundred

        if total < cost:
            print("Sorry that's not enough money. Money refunded")
            return False
        elif total - cost > 0:
            print(f"Here's your change ₹{total - cost}")
            self.__money += cost

        return True

    def validate_resources(self, ingredients) -> bool:
        for ingredient in ingredients:
            if ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry there's not enough {ingredient}")
                return False

        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]

        return True

    def make_coffee(self, coffee):
        if not self.validate_resources(MENU[coffee]['ingredients']) or not self.collect_money(MENU[coffee]["cost"]):
            return

        print(f"Here's your {coffee}☕. Enjoy 😄")

    def process_input(self, usr_in):
        if usr_in == "report":
            print(
                f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}mg\nMoney: ₹{self.__money}")

        else:
            self.make_coffee(usr_in)

    def __init__(self):
        while True:
            self.__clear_console()
            print(logo)
            user_input = input(
                "What would you like? (espresso/latte/cappuccino): ").lower()

            if not user_input in ['report', 'off'] and not user_input in MENU:
                print("Please enter a beverage from the menu. ")
                input("press enter to continue")
                continue

            if user_input == "off":
                print("Turning off the machine ...")
                break

            self.process_input(user_input)
            input("press enter to continue")


if __name__ == "__main__":
    CoffeeMachine()
    print("\nThank you for using my coffee machine :)\n\t --MO (Github @1Hanif1)")
