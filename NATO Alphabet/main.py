import pandas as PD
data = PD.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (_, row) in data.iterrows()}

while True:
    user_input = input("Enter a word or type '!exit' to exit\n>> ").upper()
    try:
        if user_input == "!EXIT":
            break
        result = [data_dict[letter] for letter in user_input]
        print(result)
    except Exception:
        print("Please provide a valid word :(")
        continue
