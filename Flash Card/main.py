from tkinter import *
from tkinter import messagebox
import pandas as PD
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 50, "bold")

language = None
word = None
french_word = None
english_word = None
data_list = None
state = False
after_function = None
data_list = []
to_learn_list = []
# --------------------------------- READ  CSV --------------------------------- #


# Main Screen ✅ Function

def start_game():
    global state, data_list

    try:
        open("./data/words_to_learn.csv", "r")
        data = PD.read_csv("./data/words_to_learn.csv")
        print("Works")
    except FileNotFoundError:
        data = PD.read_csv("./data/french_words.csv")
    finally:
        data_list = [(row.French, row.English) for (_, row) in data.iterrows()]

    right_btn.config(command=show_french_word)
    show_french_word()


# Main Screen ❌ Function

def reset():
    global data_list
    data = PD.read_csv("./data/french_words.csv")
    data_list = [(row.French, row.English) for (_, row) in data.iterrows()]
    show_french_word()


# ❌ When Word is guessed wrong

def wrong():
    global state
    to_learn_list.append((french_word, english_word))
    wrong_btn.config(command=None)
    canvas.delete("all")
    state = False
    window.after_cancel(after_function)
    show_french_word()


# ✅ When Word is guessed Right

def correct():
    global state
    data_list.remove((french_word, english_word))
    right_btn.config(command=show_french_word)
    canvas.delete("all")
    state = False
    window.after_cancel(after_function)
    show_french_word()


# Handle Main Gameplay

def show_english_word():
    global state
    canvas.delete("all")
    canvas.create_image(400, 263, image=card_back_image)
    canvas.create_text(400, 150, text=f"English", font=LANGUAGE_FONT)
    canvas.create_text(400, 263, text=f"{english_word}", font=WORD_FONT)


def show_french_word():
    global french_word, english_word, state, after_function
    if state == True:
        return

    if len(data_list) <= 0:
        canvas.create_image(400, 263, image=card_front_image)
        canvas.create_text(400, 150, text=f"All Cards Over",
                           font=LANGUAGE_FONT)
        canvas.create_text(
            400, 263, text=f"All missed words stored for revision next time", font=LANGUAGE_FONT)
        store_missed_words()
        return

    state = True

    right_btn.config(command=correct)
    wrong_btn.config(command=wrong)

    french_word, english_word = random.choice(data_list)
    canvas.delete("all")
    canvas.create_image(400, 263, image=card_front_image)
    canvas.create_text(400, 150, text=f"French", font=LANGUAGE_FONT)
    canvas.create_text(400, 263, text=f"{french_word}", font=WORD_FONT)
    after_function = window.after(ms=3000, func=show_english_word)


# Stores Missed words in a CSV
def store_missed_words():

    missed_words_dict = {
        "French": [],
        "English": [],
    }
    for french_word, english_word in to_learn_list:
        missed_words_dict["French"].append(french_word)
        missed_words_dict["English"].append(english_word)

    data = PD.DataFrame(missed_words_dict)
    data.to_csv("./data/words_to_learn.csv")


# --------------------------------- UI LAYOUT --------------------------------- #
window = Tk()
window.title("Flash Card - 100 French word ~ Mo (@Github: 1Hanif1)")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)


card_back_image = PhotoImage(file="./images/card_back.png")
card_back = canvas.create_image(400, 263, image=card_back_image)

card_front_image = PhotoImage(file="./images/card_front.png")
card_front = canvas.create_image(400, 263, image=card_front_image)

language = canvas.create_text(
    400, 150, text=f"French Words Flash Card", font=LANGUAGE_FONT)
word = canvas.create_text(
    400, 263, text="Press ✅ to start for missed words\nPress ❌ to reset cards", font=LANGUAGE_FONT)

canvas.grid(column=0, row=0, columnspan=5)

# Buttons
cross_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=cross_image, highlightthickness=0, borderwidth=0)
wrong_btn.config(command=reset)
wrong_btn.grid(column=1, row=1)

tickmark_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=tickmark_image, highlightthickness=0, borderwidth=0)
right_btn.config(command=start_game)
right_btn.grid(column=3, row=1)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        for french_word, english_word in data_list:
            to_learn_list.append((french_word, english_word))
        store_missed_words()
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
