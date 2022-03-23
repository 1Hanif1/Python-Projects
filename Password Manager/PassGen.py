import random


class PasswordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def get_password(self):
        """
        Randomly Generates a password of length 12 - 18 characters
        """
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)
        self.__password = self.generatePassword(
            nr_letters,
            nr_symbols,
            nr_numbers
        )
        return self.__password

    def get_custom_password(self):
        """ Asks the user for number of letter, symbols and numbers they want in the password\
            and generates a password accordingly
        """
        nr_letters = int(input("Enter number of letters: "))
        nr_symbols = int(input("Enter number of symbols: "))
        nr_numbers = int(input("Enter number of numbers: "))
        self.__password = self.generatePassword(
            nr_letters,
            nr_symbols,
            nr_numbers
        )
        return self.__password

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
    obj = PasswordGenerator()
    print(obj.get_password())
    print(obj.get_custom_password())
