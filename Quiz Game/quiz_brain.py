class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def is_still_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} : {current_question.text} ? (True / False) :  ")
        self.check_answer(answer, current_question.answer)

    def end_case(self):
        if self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was : ( {self.score} / {len(self.question_list)} )")

    def check_answer(self, answer, current_question):
        if answer.lower() == current_question.lower():
            self.score += 1
            print("Your answer is right")
        else:
            print(f"Your answer is  wrong , the right answer is {current_question}")
        print(f"Your score is {self.score} / {self.question_number}")
        print("\n")