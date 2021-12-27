class TipCalculator():
    def __init__(self):
        print("------Welcome to the tip calculator------")
        bill = float(input('What is the total bill? ₹'))
        percentage = float(
            input("What percentage of tip would you like to give? 10, 12 or 15?: "))
        num_people = int(input('How many people to split the bill?: '))
        tip = self.calcTip(bill, num_people, percentage)
        print(f"Each person should pay ₹{tip}")

    def calcTip(self, bill, num_people, percentage=0):
        tip = bill * (percentage / 100)
        total = bill + tip
        split_per_person = '{:.2f}'.format(total / num_people)
        return split_per_person


if __name__ == '__main__':
    TipCalculator()
