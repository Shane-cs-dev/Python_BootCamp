THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")
LABEL_FONT = ("Arial", 15, "italic")

from tkinter import *
from quiz_brain import QuizBrain

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window= Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=30, pady=20)
        ###################################
        self.canvas = Canvas(bg="White", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="This is the first question!", width=280, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        ###################################
        self.true_button_image = PhotoImage(file="../quizzler-app-start/images/true.png")
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)
        self.false_button_image = PhotoImage(file="../quizzler-app-start/images/false.png")
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)
        ###################################
        self.score = 0
        self.score_label = Label(text=f"Score={self.score}", fg="White", bg=THEME_COLOR, font=LABEL_FONT)
        self.score_label.grid(row=0, column=1)



        self.get_next_question()




        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            print(f"You finish all the questions!! \nYour final score is {self.score}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.score+=1
            self.score_label.config(text=f"Score={self.score}")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)



