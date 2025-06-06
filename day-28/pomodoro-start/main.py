from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = "Time New Roman", 30, "bold"
BUTTON_FONT = "Time New Roman", 10, "bold"
reps = 0
timer = "None"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=50, bg=YELLOW)
window.title("Pomodore")

#####Tomato Picture#####
canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_image)
canvas_text = canvas.create_text(105, 130, text="25:00", fill= "White", font=FONT)
canvas.grid(row=2, column=2, pady=10)

#####Timer label#####
label = Label(text="Timer", fg="GREEN", font=FONT, bg=YELLOW)
label.grid(row=0, column=2)

####Check Label####(✔)
check_label = Label(fg=GREEN, font=FONT, bg=YELLOW)
check_label.grid(row=4, column=2)

#####Functionality creation#####
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break!", fg=RED)
    if reps % 2 ==0:
        count_down(break_sec)
        label.config(text="Break!", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(time):

    time_min = math.floor(time/60)
    time_sec = int(time % 60)
    if time_sec < 10:
        time_sec = f"0{time_sec}"

    canvas.itemconfig(canvas_text, text=f'{time_min}:{time_sec}')
    if time > 0:
        print(time)
        global timer
        timer = window.after(1000, count_down, time-1)
    if time ==0:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_label.config(text=mark)
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    #Time text to 00:00
    canvas.itemconfig(canvas_text, text="25:00")
    #title text to "Timer"
    label.config(text="Timer", fg=GREEN)
    #reset check mark
    check_label.config(text="")
    global reps
    reps = 0

#####Start/Reset button#####
start_button = Button(text="Start", width=5, height=1, font=BUTTON_FONT, command=start_timer)
start_button.grid(row=3, column=0)
reset_button = Button(text="Reset", width=5, height=1, font=BUTTON_FONT, command=reset)
reset_button.grid(row=3, column=3)
















window.mainloop()