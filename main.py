from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
        quiz.next_question()

print(f"You have completed the quiz. \n Your final score was: {quiz.score} / {quiz.question_number} ")