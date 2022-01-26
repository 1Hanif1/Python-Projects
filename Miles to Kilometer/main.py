from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=10)


def calculate():
    try:
        value = int(user_input.get())
        value = round(value * 1.609)
        label_result.config(text=f"{value}", foreground="green")
    except Exception:
        label_result.config(text=f"Invalid", foreground="red")


user_input = Entry(width=5)
user_input.grid(column=1, row=0)

calc_button = Button(text="calculate", command=calculate)
calc_button.grid(column=1, row=2)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_result = Label(text="")
label_result.grid(column=1, row=1)

label_format = Label(text="is equal to")
label_format.grid(column=0, row=1)


window.mainloop()
