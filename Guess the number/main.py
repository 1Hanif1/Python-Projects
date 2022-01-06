from art import logo
from random import randint


class GuessTheNumber():
    def start(self, mode):
        guessed_number = randint(1, 100)
        attempt = 10 if mode == "easy" else 5

        while attempt > 0:

            print(f"You have {attempt} guess left.")

            try:
                user_guess = int(input("Make a guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if user_guess > guessed_number:
                print("Too High")
                attempt -= 1
                continue

            elif user_guess < guessed_number:
                print("Too Low")
                attempt -= 1
                continue

            else:
                print("You guessed it ;)")
                return

        print(
            f"Oops No more attempts left. You Lost :(.\n The number was {guessed_number}")

    def __init__(self):
        print(logo)
        print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100")
        while True:

            difficulty = input(
                "Choose a difficulty, type 'easy' or 'hard': ").lower()

            if difficulty not in ['easy', 'hard']:
                print("please enter valid input")
                continue

            self.start(difficulty)

            choice = input("Want to play again?[y/n]: ").lower()
            if choice == "y":
                continue
            break


if __name__ == '__main__':
    GuessTheNumber()
    print("Thank for playing 'Guess the number' :)\n\t--MO (Github: @1Hanif1)")
