from data import QUESTION_DATA
from ui import QuizInterface
from question_model import Question
from quiz_brain import QuizBrain


#initialize global variable
QUESTION_BANK = []


#loop over data in data.py and format for QuizBrain class
for question in QUESTION_DATA:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    QUESTION_BANK.append(new_question)


#placed below for loop to ensure appended questions are added accordingly
QUIZ = QuizBrain(QUESTION_BANK)
QUIZ_UI = QuizInterface(QUIZ)


#start game loop
try:
    while QUIZ.playing():
        QUIZ.next_question()

except KeyboardInterrupt:
    print('\nSee you later.')

print('You\'ve completed the quiz')
print(f'Your final score was: {QUIZ.score}/{QUIZ.question_number}')