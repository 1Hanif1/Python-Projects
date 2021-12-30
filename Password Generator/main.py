import random


class PasswordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self) -> None:
        print("-------------- Password Generator --------------")
        while True:
            try:
                nr_letters = int(
                    input("\nHow many letters would you like in your password?\n"))
                nr_symbols = int(input(f"How many symbols would you like?\n"))
                nr_numbers = int(input(f"How many numbers would you like?\n"))
            except ValueError:
                print("Please provide a valid input ...")
                continue
            password = self.generatePassword(
                nr_letters, nr_symbols, nr_numbers)
            print(f"Your generated password: {password}")
            choice = input(
                '\nWant to generate another password? [y/n]: ').lower()
            if choice == 'n':
                break
        print(
            "\nThank you for using my password generator :) \n\t-- Mo (Github: @1Hanif1) ")

    def generatePassword(self, num_letters, num_symbols, num_numbers) -> str:
        password = ""
        for _ in range(num_letters):
            password += self.letters[random.randint(0, len(self.letters) - 1)]

        for _ in range(num_symbols):
            password += self.symbols[random.randint(0, len(self.symbols) - 1)]

        for _ in range(num_numbers):
            password += self.numbers[random.randint(0, len(self.numbers) - 1)]

        password = self.randomisePassword(password)
        return password

    def randomisePassword(self, password) -> str:
        randomised_password = ""
        password_chars = [char for char in password]
        random.shuffle(password_chars)
        for char in password_chars:
            randomised_password += char
        return randomised_password


if __name__ == '__main__':
    PasswordGenerator()
