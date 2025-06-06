from tkinter import *

FONT = "Time New Roman", 10, "bold"
##########################

##########################
window = Tk()
window.title("Converter")
window.wm_minsize(width=200, height=200)
window.config(padx=50, pady=50)

#Label (is equal to)
equal = Label(text="is equal to", font=FONT)
equal.grid(row=11, column=20)

#Label (Celsius)
celsius = Label(text="Celsius", font=FONT)
celsius.grid(row=10, column=100)

#Label (Fahrenheit)
fahrenheit = Label(text="Fahrenheit", font=FONT)
fahrenheit.grid(row=11, column=100)

#Label (Converted answer)
converted_degree = Label(text="0", font=FONT)
converted_degree.grid(row=11, column=50)

#Entry
insert = Entry(width=10, justify="center")
insert.grid(row=10, column=50)
###########################
def convert():
    new_data= (float(insert.get()) * 9/5) + 32
    converted_degree.config(text=new_data)

###########################
#Button
quit_button = Button(text="Quit", width=5 ,command=window.destroy)
quit_button.grid(row=100, column=100)

#calculate button
cal_button = Button(text="Calculate", command=convert)
cal_button.grid(row=100, column=50)































window.mainloop()