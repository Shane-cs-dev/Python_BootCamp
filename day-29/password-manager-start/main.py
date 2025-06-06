from tkinter import *
from tkinter import messagebox
import random


import pyperclip
import json
FONT = "Time new roman", 10, "bold italic"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def record_information():
    entry_web = website_input.get().upper()
    entry_username = username_pw_input.get()
    entry_pw = password_input.get()
    new_data = {
        entry_web:{
            "email": entry_username,
            "password":entry_pw,
        }
    }
    if entry_pw == "" or entry_username == "" or entry_web == "":
        messagebox.showinfo(title="Oops", message="Don't leave the entry empty")
    else:
        try:
            with open("data.json", mode="r") as new_json:
                try:
                    #Load data
                    data = json.load(new_json)
                except json.JSONDecodeError:
                    # Handle empty or invalid JSON file
                    data = {}
        except FileNotFoundError:
            with open("data.json", mode="w") as new_json:
                json.dump(new_data, new_json, indent=4)
        else:
            #Write data
            data.update(new_data)
            with open("data.json", mode="w") as new_json:
                #Save data
                json.dump(data, new_json, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- Search button -------------------------- #
def search():
    try:
        with open("data.json", mode="r") as json_data:
            read_data = json.load(json_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
            try:
                search_source = website_input.get().upper()
                email = read_data[search_source]["email"]
                password = read_data[search_source]["password"]
            except KeyError:
                messagebox.showinfo(title="Oops", message="We don't find this website name")
                website_input.delete(0, END)
            else:
                messagebox.showinfo(title="Here you are", message=f"username/email: {email}\npassword: {password}")
                username_pw_input.delete(0, END)
                password_input.delete(0, END)
                username_pw_input.insert(0, email)
                password_input.insert(0, password)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="White", padx=50, pady=50)

#Canvas
canvas = Canvas(bg="White", height=220, width=220, highlightthickness=0, highlightcolor="Black")
file_path = "../password-manager-start/logo.png"
security_image= PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=security_image)
canvas.grid(row=0, column=1)
#Label
website = Label(text="Website:", font=FONT, bg="White")
website.grid(row=1, column=0)
user_name_pw = Label(text="Email/Username:", font=FONT, bg="White")
user_name_pw.grid(row=2, column=0)
pw = Label(text="Password:", font=FONT, bg="White")
pw.grid(row=3, column=0)
#Entry
website_input = Entry(width=35, justify="left", border=2)
website_input.grid(row=1, column=1)
website_input.focus()
username_pw_input = Entry(width=35, justify="left", border=2)
username_pw_input.grid(row=2, column=1)
username_pw_input.insert(0, "shane09220532@gmail.com")
password_input = Entry(width=35, justify="left", border=2)
password_input.grid(row=3, column=1)
#Button
generation = Button(text="Generate Password",height=1, border=0.5, command=generate_password)
generation.grid(row=3, column=2)
add_button = Button(text="Add", width=45, height=1, border=0.5, command=record_information)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", height=1, border=0.5, width=14, command=search)
search_button.grid(row=1, column=2)

















































window.mainloop()