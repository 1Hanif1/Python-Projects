from word_list import words
import random


class Hangman():
    __words = words
    __point = 6
    __stages = ['''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                =========
                ''', '''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========
                ''', '''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========
                ''', '''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========''', '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========
                ''', '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========
                ''', '''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========
                ''']

    def __init__(self) -> None:

        print('''
                 _                                             
                | |                                            
                | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                | | | | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |                      
                                   |___/                            
                        \n
        ''')
        self.__start()

    def __start(self) -> None:

        word = self.__words[random.randint(0, len(self.__words) - 1)]
        place_holder = ['_' for _ in word]
        self.__printStatus(place_holder)

        while True:
            user_input = input('\nGuess a letter: ').lower()
            place_holder = self.__validate(word, user_input, place_holder)
            self.__printStatus(place_holder)

            if self.__point <= 0:
                print("You lost (~ __ ~)")
                break
            elif not '_' in place_holder:
                print("You win (^ __ ^)")
                break

    def __validate(self, word, user_input, place_holder) -> list:

        original = [_ for _ in place_holder]

        for index, letter in enumerate(word):
            if letter == user_input:
                place_holder[index] = letter

        if original == place_holder and not user_input in place_holder:
            self.__point -= 1

        return place_holder

    def __printStatus(self, place_holder) -> None:
        string = ""
        for letter in place_holder:
            string += letter + ' '
        print(
            f"{self.__stages[self.__point]}\nword: {string}")


if __name__ == '__main__':
    while True:
        Hangman()
        choice = input('Want to Play again?[y/n]: ').lower()
        if choice == 'n':
            print(
                "GAME OVER\nThank you for playing this game :) \n\t-- Mo (Github: @1Hanif1) ")
            break
