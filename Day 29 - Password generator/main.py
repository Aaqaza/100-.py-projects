from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_entry.delete(0, END)

    password_list = []
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]

    # Or for better understanding
    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)
    #
    # p_letters = [choice(letters) for _ in range(nr_letters)]
    # p_symbols = [choice(symbols) for _ in range(nr_symbols)]
    # p_numbers = [choice(numbers) for _ in range(nr_numbers)]
    #
    # password_list = p_letters + p_symbols + p_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # To automatically copy it to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(message="Please don't leave any fields empty")

    else:
        messagebox.askokcancel(message=f"These are the details entered : \n\nEmail : {email} "
                                       f"Website : {website}\nPassword : {password}"
                                       f"\n\nIs it okay to save?")

        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_title = Label(text="Website:")
website_title.grid(column=0, row=1)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
website = website_entry.get()

email_title = Label(text="Email/Username:")
email_title.grid(column=0, row=2)

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "aaqil@test.com")
email = email_entry.get()

password_title = Label(text="Password:")
password_title.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)
password = password_entry.get()

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

Add_button = Button(text="Add", width=37, command=save)
Add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
