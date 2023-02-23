from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_object = Question(q_text=text, q_answer=answer)
    question_bank.append(question_object)

quizBrain = QuizBrain(question_bank)
while quizBrain.is_still_questions():
    quizBrain.next_question()
quizBrain.end_case()