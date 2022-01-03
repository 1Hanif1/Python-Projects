from os import system, name
from art import logo


class SecretAuction():
    __bidders = {}
    __intro = "\nWelcome to the secret auction program! Bidding made anonymous!\n\
Instructions: \n- Enter your name and place your bid.\n- prompt will ask you, if there's any more bidders? \
enter 'yes' if there are. \n- Your bid ammount will be hidden.\n- Next bidder can then come and bid their amount."

    def __clearConsole(self): return system('cls') if name in [
        'nt', 'dos'] else system('clear')

    def __init__(self) -> None:
        print(logo)
        while True:
            print(self.__intro)
            print("".rjust(50, "-"))
            boolean_value = self.__input()
            if not boolean_value:
                self.__auction()
                return
            else:
                self.__clearConsole()
                continue

    def __input(self):
        try:
            name = input("\nEnter your name: ")
            bid = int(input("Enter your bid: ₹"))

            if bid <= 0:
                raise ValueError

            self.__bidders[name] = bid

            while True:
                more_bidders = input(
                    "Are there any more bidders? Type 'yes' or 'no': ").lower()
                if more_bidders == "no":
                    return False
                elif more_bidders == "yes":
                    return True
                else:
                    print("Invalid Input\n")
                    continue
        except ValueError:
            print("Please provide a valid bidding ammount!")
            input("\nPress ENTER to continue")
            return True

    def __auction(self):
        winner = ""
        winner_bid = 0

        for bidder, bid in self.__bidders.items():
            if bid > winner_bid:
                winner = bidder
                winner_bid = bid

        self.__clearConsole()
        print(f"\nThe winner is {winner} with a bid of ₹{winner_bid}.")


if __name__ == '__main__':
    SecretAuction()
    print(
        "\nThank you for using my secret auction program :) \n\t-- Mo (Github: @1Hanif1) ")
