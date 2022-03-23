
from email import message
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    try:
        with open("data.json", mode="r") as file:
            old_data = json.load(file)

    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_data, file)

    else:
        if website in old_data:

            user_choice = messagebox.askyesno(
                title=f"Warning", message=f"{website} credentials already exist\nWant to override them?")

            if not user_choice:
                return

        old_data.update(new_data)
        with open("data.json", mode="w") as file:
            json.dump(old_data, file)

    website_input.delete(0, END)
    password_input.delete(0, END)

    messagebox.showinfo(
        title="Success", message="Credentials added successfully 🥳")

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_pass():
    website = website_input.get()

    if len(website) <= 0:
        messagebox.showerror(
            title="Error", message="Please enter some website name")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data = data[website]

            data_email = data["email"]
            data_pass = data["password"]
    except FileNotFoundError:
        messagebox.showerror(
            title="Oops", message="There are no saved passwords ☹️")
    except KeyError:
        messagebox.showerror(
            title="Oops", message="No password found for this website")
    else:
        messagebox.showinfo(title=f"{website} credentials",
                            message=f"Username/Email: {data_email}\nPassword: {data_pass}")


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
gen_pass = Button(text="Generate Password",
                  command=generate_password)
add_pass = Button(text="Add", width=30, command=add_password)
search_pass = Button(text="Search", width=15, command=search_pass)

# INPUT
website_input = Entry(width=39)
username_input = Entry(width=58)
password_input = Entry(width=39)

# Adding widgets to window
canvas.grid(column=0, row=0, columnspan=3)

website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1)
website_input.focus()

username_label.grid(column=0, row=2)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(END, "yourname@example.com")

password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3)

gen_pass.grid(column=2, row=3)
add_pass.grid(column=1, row=5)
search_pass.grid(column=2, row=1)

window.mainloop()
