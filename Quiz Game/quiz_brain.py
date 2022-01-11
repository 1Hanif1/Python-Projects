class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}. {question.text}. (True/False)?: ")
        if self.check_answer(user_answer, question.answer):
            self.score += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right! :)")
            self.score += 1
        else:
            print("You got it wrong! :(")
        print(
            f"Correct answer: {correct_ans}\nCurrent Score: {self.score}/{self.question_number}\n")
