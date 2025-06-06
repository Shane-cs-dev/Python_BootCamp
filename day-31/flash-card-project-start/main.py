from tkinter import *
import pandas
import random
 #-------------------Input----------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT="Ariel",40, "italic"
FONT_2="Ariel",60, "bold italic"
random_card = 0
#####################################################
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0, highlightbackground="Black", highlightcolor="Blue")

#-------------------------------------Read csv.file-------------------------------------------------#
new_word_file = pandas.read_csv("../flash-card-project-start/data/french_words.csv")
new_word_dict = {row.French:row.English for (index, row) in new_word_file.iterrows()}
# print(new_word_dict)
word_dict = {
    "French": list(new_word_dict.keys()),
    "English": list(new_word_dict.values())
}
# print(word_dict)
# print(list(new_word_dict.keys()))
#-------------------------------------Generate random french word-------------------------------------------------#

def next_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_number = random.randint(0, 100)
    current_french_card = word_dict["French"][random_number]
    print(current_french_card)
    card_front.itemconfig(card_title, text="French", fill="black")
    card_front.itemconfig(card_word, text=current_french_card, fill="Black")
    card_front.itemconfig(front_image, image=front)
    flip_timer= window.after(ms=3000, func=flip_card)

#-------------------------------------Generate random french word-------------------------------------------------#
def flip_card():
    random_english_word = word_dict["English"][random_card]
    card_front.itemconfig(card_title, text="English", fill="White")
    card_front.itemconfig(front_image, image=back)
    card_front.itemconfig(card_word, text=random_english_word, fill="White")

#-------------------------------------Modified csv file-------------------------------------------------#





###Canvas
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
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=2, column=1)
wrong_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=2, column=2)
#Label
# # title = Label(text="title", font=FONT, bg="White")
# card_front.create_text(400, 150, text="Title", font=FONT, bg="White")
# word = Label(text="Word", font=FONT_2, bg="White")
# card_front.create_window(390, 270, window=word)




next_card()
flip_timer = window.after(3000, func=flip_card)



































































window.mainloop()