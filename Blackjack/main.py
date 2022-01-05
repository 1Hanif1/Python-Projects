from art import logo
from random import randint


class BlackJack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []
    u_score = c_score = 0

    def reset(self):
        self.user_cards = []
        self.comp_cards = []
        self.u_score = self.c_score = 0

    def start(self):
        self.reset()
        for _ in range(2):
            self.user_cards.append(self.draw_card())
            self.comp_cards.append(self.draw_card())

    def calc_score(self,  scores):
        total = 0
        for score in scores:
            total += score
        return total

    def print_full_stat(self):
        print(
            f"Player's cards: {self.user_cards}\tPlayer score: {self.calc_score(self.user_cards)}\nComputer's cards: {self.comp_cards}\tComputer Score: {self.calc_score(self.comp_cards)}")

    def print_stat(self):
        print(
            f"Player's cards: {self.user_cards}\tPlayer score: {self.calc_score(self.user_cards)}\nComputer's first card: {self.comp_cards[0]}")

    def draw_card(self):
        return self.cards[randint(0, len(self.cards) - 1)]

    def validate_score(self, score):
        if score > 21:
            return False
        return True

    def pass_func(self):
        self.print_full_stat()

        self.c_score = self.calc_score(self.comp_cards)
        self.u_score = self.calc_score(self.user_cards)

        if self.c_score == self.u_score:
            print("It's a draw 😑")
            return
        elif not self.validate_score(self.c_score) or self.c_score < self.u_score:
            print('You win 🥳')
            return
        print('You Lost 😭')
        return

    def draw_func(self):
        self.user_cards.append(self.draw_card())
        self.u_score = self.calc_score(self.user_cards)
        if not self.validate_score(self.calc_score(self.user_cards)):
            self.print_full_stat()
            print("BUST! You lost 😭")
            return False
        self.print_stat()
        return True

    def __init__(self):
        self.start()
        self.print_stat()
        while True:
            choice = input("Type 'y' to draw a card or 'n' to pass: ").lower()
            if choice == 'y':
                if self.draw_func():
                    continue
                break
            elif choice == 'n':
                while self.calc_score(self.comp_cards) < 17:
                    self.comp_cards.append(self.draw_card())
                self.pass_func()
                break
            else:
                print('Please provide a valid input 😓')
                continue


if __name__ == '__main__':
    while True:
        user_input = input('\nWant to play BlackJack?[y/n]: ').lower()
        if user_input == 'y':
            print(logo)
            BlackJack()
            continue
        else:
            break
    print(
        "\nThank you for playing Black Jack :) \n\t-- Mo (Github: @1Hanif1) ")
