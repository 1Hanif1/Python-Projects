
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


class PasswordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self):

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        self.password = self.generatePassword(
            nr_letters, nr_symbols, nr_numbers)

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


def generate_password():
    PSWD = PasswordGenerator()
    password_input.delete(0, END)
    password_input.insert(END, PSWD.password)
    pyperclip.copy(PSWD.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    for input in [website_input, username_input, password_input]:
        if len(input.get()) <= 0:
            messagebox.showerror(
                title="Input Fields Empty", message="Input Fields can't be empty 😥")
            return

    user_input = messagebox.askokcancel(
        title=website, message=f"Details entered\nEmail:{username}\nPassword:{password}\nIs it okay to save?")
    if not user_input:
        return

    with open("your_credentials.txt", mode="a") as file:
        file.write(
            f"website: {website} | username: {username} | password: {password} \n\n")
        website_input.delete(0, END)
        username_input.delete(0, END)

    messagebox.showinfo(
        title="Success", message="Credentials added successfully 🥳")


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = ('Arial', 10, "bold")

window = Tk()
window.title("Password manager ~ Mo (Github: @1Hanif1)")
window.config(padx=50, pady=50)

# LOGO
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

# LABELS
website_label = Label(text="website:", font=FONT_NAME)
username_label = Label(text="Email/Username:", font=FONT_NAME)
password_label = Label(text="Password:", font=FONT_NAME)

# BUTTONS
gen_pass = Button(text="Generate Password", width=30,
                  command=generate_password)
add_pass = Button(text="Add", width=30, command=add_password)

# INPUT
website_input = Entry(width=39)
username_input = Entry(width=39)
password_input = Entry(width=39)

# Adding widgets to window
canvas.grid(column=0, row=0, columnspan=2)

website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1)
website_input.focus()

username_label.grid(column=0, row=2)
username_input.grid(column=1, row=2)
username_input.insert(END, "yourname@example.com")

password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3)

gen_pass.grid(column=1, row=4)
add_pass.grid(column=1, row=5)

window.mainloop()
