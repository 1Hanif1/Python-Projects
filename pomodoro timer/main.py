from cgitb import text
from tkinter import *

from pygame import font
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_RUNNING = False
reps = 0
checkmark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global TIMER_RUNNING, reps, checkmark
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    TIMER_RUNNING = False
    checkmark = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def start_timer():

    global TIMER_RUNNING
    global reps
    reps += 1

    if not TIMER_RUNNING:
        TIMER_RUNNING = True

        time = 0

        if reps % 2 == 0:
            add_checkmark()

        if reps % 8 == 0:
            time = LONG_BREAK_MIN
            timer_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            time = SHORT_BREAK_MIN
            timer_label.config(text="Break", fg=PINK)
        else:
            time = WORK_MIN
            timer_label.config(text="Work", fg=GREEN)

        raise_above_all()

        count_down(time * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def add_checkmark():
    global checkmark
    checkmark += "✅"
    checkmark_label.config(text=checkmark)


def count_down(count):
    global timer

    minute = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if minute < 10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")

    if count <= 0:
        global TIMER_RUNNING
        TIMER_RUNNING = False
        if reps < 8:
            start_timer()
        else:
            timer_label.config(text="Timer", fg=GREEN)
        return

    timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer ~ Github: @1Hanif1")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Tomato Image
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 132, text="00:00", fill="white",
                                font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

#  Buttons
start_btn = Button(text="Start", font=(
    FONT_NAME, 10, "bold"), fg=RED, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", font=(
    FONT_NAME, 10, "bold"), fg=RED, command=reset_timer)
reset_btn.grid(column=2, row=2)

#  Checkmark
checkmark_label = Label(font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
