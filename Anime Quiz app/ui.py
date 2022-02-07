
from cgitb import text
from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain


THEME_COLOR = "#F6C5AF"


class QuizUI():
    def get_next_question(self):
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(
                self.canvas_text, text=f"Quiz Completed :)\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

            self.true_btn.config(state="disabled")

            self.false_btn.config(state="disabled")

            return

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)

    def canvas_reset(self):
        self.canvas.config(bg="white")
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, func=self.canvas_reset)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true(self):
        result = self.quiz.check_answer("True")
        self.update_score()
        self.give_feedback(result)

    def false(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Anime Quiz ~ Mo (Github: @1Hanif1")
        self.window.config(bg=THEME_COLOR, width=300,
                           height=300, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", font=("Arial", 16, "bold"),
                                 bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.canvas_text = self.canvas.create_text(
            (150, 125), text="Here's Some redundant text cause why not", font=("Arial", 16, "normal"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, width=100,
                               height=90, highlightthickness=0, command=self.true)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=false_img, width=100,
                                height=90, highlightthickness=0, command=self.false)

        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


# QuizUI()
