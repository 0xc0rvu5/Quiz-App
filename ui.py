from tkinter import *
from quiz_brain import QuizBrain


#initialize global variable
THEME_COLOR = '#375362'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz Me Please')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, height=540, width=300)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Random text present',
            fill=THEME_COLOR,
            font=('Ariel', 12, 'italic'))
        correct = PhotoImage(file='images/true.png')
        incorrect = PhotoImage(file='images/false.png')
        self.correct_button = Button(image=correct, highlightthickness=0, command=self.correct_press)
        self.incorrect_button = Button(image=incorrect, highlightthickness=0, command=self.incorrect_press)
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.score_label.grid(pady=20, row=0, column=1)
        self.correct_button.grid(pady=20, row=2, column=0)
        self.incorrect_button.grid(pady=20, row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        '''Get next question functionality.'''
        self.canvas.config(bg='white')
        if self.quiz.playing():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have completed the quiz.')
            self.correct_button.config(state='disabled')
            self.incorrect_button.config(state='disabled')


    def correct_press(self):
        '''Correct answer functionality.'''
        self.give_feedback(self.quiz.check_answer('True'))


    def incorrect_press(self):
        '''Incorrect answer functionality.'''
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self, is_right):
        '''Give a visual confirmation if answer is correct/incorrect.'''
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)