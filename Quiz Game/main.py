from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


class Game:
    def __init__(self):
        question_bank = []

        for question in question_data:
            new_question = Question(
                question["question"], question['correct_answer'])
            question_bank.append(new_question)

        Quiz = QuizBrain(question_bank)

        while Quiz.still_has_questions():
            Quiz.next_question()

        print(
            f"You have completed the quiz 🥳\nYour final score was: {Quiz.score}/{Quiz.question_number}")


if __name__ == '__main__':
    Game()
    print("Thank you trying out the quiz game :)\n\t --MO (Github @1Hanif1)")
