from tkinter import *
import pandas
import random
 #-------------------Input----------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT="Ariel",40, "italic"
FONT_2="Ariel",60, "bold italic"
random_card = {}
to_learn_dict = {}
#####################################################
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0, highlightbackground="Black", highlightcolor="Blue")

#-------------------------------------Read csv.file-------------------------------------------------#
try:
    new_word_file = pandas.read_csv("word_to_learn.csv")
except FileNotFoundError:
    new_word_file = pandas.read_csv("../flash-card-project-start/data/french_words.csv")
    # print(new_word_file)
    to_learn_dict = new_word_file.to_dict(orient="records")
else:
    to_learn_dict = new_word_file.to_dict(orient="records")

#-------------------------------------Generate random french word-------------------------------------------------#

def next_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(to_learn_dict)
    current_french_card = random_card["French"]
    # print(current_french_card)
    card_front.itemconfig(card_title, text="French", fill="black")
    card_front.itemconfig(card_word, text=current_french_card, fill="Black")
    card_front.itemconfig(front_image, image=front)
    flip_timer= window.after(ms=3000, func=flip_card)

#-------------------------------------Generate random french word-------------------------------------------------#
def flip_card():
    current_english_word = random_card["English"]
    card_front.itemconfig(card_title, text="English", fill="White")
    card_front.itemconfig(front_image, image=back)
    card_front.itemconfig(card_word, text=current_english_word, fill="White")

#-------------------------------------Modified csv file-------------------------------------------------#
def click_know():
    to_learn_dict.remove(random_card)
    next_card()
    word_to_learn_df = pandas.DataFrame(to_learn_dict)
    word_to_learn_df.to_csv("data/word_to_learn.csv", index=False)





###Cancas
card_front = Canvas(bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)
front = PhotoImage(file="../flash-card-project-start/images/card_front.png")
front_image = card_front.create_image(410, 270, image=front)
card_title = card_front.create_text(400, 150, text="Title", font=FONT)
card_word = card_front.create_text(390, 270, text="Word", font=FONT_2)
card_front.grid(row=1, column=1, columnspan=2)
# card_back = Canvas(bg=BACKGROUND_COLOR, height=526, width=800)
back = PhotoImage(file="../flash-card-project-start/images/card_back.png")
# card_back.create_image(410, 270, image=back)
# card_back.grid(row=1, column=1, columnspan=2)
###Button
right_image = PhotoImage(file="../flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=click_know)
right_button.grid(row=2, column=2)
wrong_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=2, column=1)
#Label
# # title = Label(text="title", font=FONT, bg="White")
# card_front.create_text(400, 150, text="Title", font=FONT, bg="White")
# word = Label(text="Word", font=FONT_2, bg="White")
# card_front.create_window(390, 270, window=word)



flip_timer = window.after(3000, func=flip_card)
next_card()
# word_to_learn_df = pandas.DataFrame(new_word_dict)
# word_to_learn_df.to_csv("word_to_learn.csv", index=False)



































































window.mainloop()