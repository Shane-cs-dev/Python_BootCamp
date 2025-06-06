from tkinter import *

def button_click():
    print("Happy birthday")
    my_label.config(text=insert.get())

window = Tk()
window.title("GUI program")
window.wm_minsize(width=800, height=500)
window.config(padx=30, pady=30)


#Label
my_label = Label(text="LABEL", font=("Time New Roman", 20, "bold"))
my_label.config(text="I'm not LABEL")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

#Entry
insert = Entry(width=15)
insert.grid(column=10, row=10)

#Button
button = Button(text="Hit me!", command= button_click)
button.grid(column=5, row=5)

new_button = Button(text="I'm new", command=button_click)
new_button.grid(column=7, row=0)





















window.mainloop()