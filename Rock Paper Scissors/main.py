import random


class RockPaperScissors():
    rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

    paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  '''

    scissors = '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''

    signs = [rock, paper, scissors]

    def __init__(self):
        print("---------- Rock x Paper x Scissors ----------")
        state = True
        while state:
            try:
                choice = int(input(
                    '\nWhat do you choose?\nType 1 for Rock\nType 2 for Paper\nType 3 for Scissors\nyour choice: '))
            except ValueError:
                print("\nPlease enter a number :(")
                continue
            if choice < 0 or choice > 3:
                print("Invalid Choice :(")
                continue
            else:
                self.game(choice)
            restart = input('Wanna play again?[y/n]: ').upper()
            if restart == 'N':
                state = False

    def game(self, choice):
        choice -= 1
        computer = random.randint(0, 2)
        print(
            f"{self.signs[choice]}\nComputer Choosed:\n{self.signs[computer]}")
        if choice == computer:
            print("It's a Draw (-__-)")
        elif (choice == 0 and computer == 2) or (choice == 2 and computer == 0):
            if choice < computer:
                print("You win! (^__^)")
            else:
                print("You Lose! (~__~)")
        elif choice > computer:
            print("You win! (^__^)")
        else:
            print("You Lose! (~__~)")


if __name__ == '__main__':
    RockPaperScissors()
