from art import logo, vs
from game_data import data
from random import randint
from os import system, name


class HigherLower():

    def clear_console(self):
        return system('cls' if name == 'nt' else 'clear')

    def user_interface(self, acc_one, acc_two, score=0):
        self.clear_console()

        print(logo)

        if score != 0:
            print(f"You're Right :)\t Current Score: {score}")

        print(
            f"Compare A: {acc_one['name']}, a/an {acc_one['description']}, from {acc_one['country']}.")
        print(vs)
        print(
            f"Against B: {acc_two['name']}, a/an {acc_two['description']}, from {acc_two['country']}.")

        while True:
            user_input = input(
                "Who has more followers? Type 'A' or 'B': ").upper()
            if user_input not in ['A', 'B']:
                print("Please provide a valid input :(")
                continue
            break

        if user_input == 'A':
            result = acc_one if acc_one['follower_count'] > acc_two['follower_count'] else False
        else:
            result = acc_two if acc_two['follower_count'] > acc_one['follower_count'] else False

        return result

    def __init__(self):
        score = 0
        account_one = data[randint(0, len(data) - 1)]
        while True:

            account_two = data[randint(0, len(data) - 1)]

            while account_one == account_two:
                account_two = data[randint(0, len(data) - 1)]

            result = self.user_interface(account_one, account_two, score)

            if result == False:
                print(f"Sorry That's Wrong :(\tFinal Score: {score}")
                return
            account_one = result
            score += 1


if __name__ == '__main__':
    HigherLower()
    print("Thank you for playing Higher Lower :)\n\t --MO (Github: @1Hanif1")
