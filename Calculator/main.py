from art import logo


class Calculator():
    __operations = ["+", "-", "*", "/"]

    def __add(self, n1, n2):
        return n1 + n2

    def __subtract(self, n1, n2):
        return n1 - n2

    def __divide(self, n1, n2):
        return n1 / n2

    def __multiply(self, n1, n2):
        return n1 * n2

    def __performOperation(self, operand, f_num, n_num):
        result = 0

        if operand == "+":
            result = self.__add(f_num, n_num)
        elif operand == "-":
            result = self.__subtract(f_num, n_num)
        elif operand == "*":
            result = self.__multiply(f_num, n_num)
        else:
            result = self.__divide(f_num, n_num)

        return result

    def __init__(self):

        print(logo)

        while True:
            try:
                f_num = float(input("What's the first number: "))
            except ValueError:
                print("Please Provide a valid input :(")
                continue

            print("+\n-\n*\n/")
            while True:
                operand = input("Pick an operation: ")

                if not operand in self.__operations:
                    print("Please enter a valid operation")
                    continue
                try:
                    n_num = float(input("What's the next number: "))
                except ValueError:
                    print("Please Provide a valid input :(")
                    continue
                result = self.__performOperation(operand, f_num, n_num)

                print(f"{f_num} {operand} {n_num} = {result}")

                choice = input(
                    f"\nType 'y' to continue calculating with {result}\ntype 'n' to start a new calculation\ntype 'e' to exit\n>> ").lower()

                if choice == 'n':
                    break
                elif choice == 'y':
                    f_num = result
                    continue
                elif choice == 'e':
                    print("Exiting Program ...")
                    return
                else:
                    print("Invalid Input. Restarting Program ...")
                    break
            continue


if __name__ == '__main__':
    Calculator()
    print(
        "\nThank you for using my calculator program :) \n\t-- Mo (Github: @1Hanif1) ")
