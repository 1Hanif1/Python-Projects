from art import logo


class CaesarCipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self) -> None:
        print(logo)
        while True:
            print("\n------------------------------------------------------")
            usr_choice = input(
                "\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()

            if not usr_choice in ['encode', 'decode']:
                print("\nPlease provide a valid input :3")
                continue

            msg = self.__cipher(usr_choice)
            print(f"\n{usr_choice}d message: {msg}")
            restart = input(
                "\nWant to cipher/decipher again?[press n to exit]: ").lower()
            if restart == 'n':
                break

    def __input(self):
        while True:
            try:
                text = input("\nType your message: ").lower()
                shift = int(input("\nType the shift number: "))
                if shift < 0:
                    raise ValueError("\nShift can't be less than zero :(")

            except ValueError:
                print("\nPlease provide a valid input :3")
                continue

            return {'text': text, 'shift': shift}

    def __cipher(self, action):
        cipher_msg = ""
        usr_input = self.__input()

        for char in usr_input['text']:
            if not char in self.alphabet:
                cipher_msg += char
                continue
            index = self.__shift(char, usr_input['shift'], action)
            cipher_msg += self.alphabet[index]

        return cipher_msg

    def __shift(self, char, shift, action):
        index = self.alphabet.index(char)

        if action == 'encode':
            for _ in range(shift):
                if index == len(self.alphabet) - 1:
                    index = 0
                else:
                    index += 1

        else:
            for _ in range(shift):
                if index == 0:
                    index = len(self.alphabet) - 1
                else:
                    index -= 1

        return index


if __name__ == '__main__':
    CaesarCipher()
    print(
        "\nThank you for using my caesar cipher program :) \n\t-- Mo (Github: @1Hanif1) ")
