from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")


def generate_password():
    # Clears the current password entry
    password_entry.delete(0, END)

    # Generates random password with specified number of letters, numbers, and symbols
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    # Shuffles the list to make password random and secure
    shuffle(password_list)

    # Combines the shuffled list into a single string
    password = "".join(password_list)

    # Inserts the generated password into the password entry field
    password_entry.insert(0, password)

    # Automatically copies the generated password to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Data to be added to the JSON file
    new_data = {website: {"email": email, "password": password}}

    # Error handling if any of the fields are empty
    if not website or not email or not password:
        messagebox.showerror(message="Please don't leave any fields empty")
        return

    try:
        # Try to load existing data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or corrupted, initialize an empty dictionary
        data = {}

    # Check if the website already exists in the file
    if website in data:
        # Ask for confirmation before updating the existing password
        update_password = messagebox.askokcancel(
            message="Password already exists for this website. Do you want to update your password?"
        )
        if update_password:
            data[website] = new_data[website]
            messagebox.showinfo(message="Password updated successfully!")
        else:
            messagebox.showinfo(message="No changes were made.")
            return
    else:
        # Add new data
        data.update(new_data)
        messagebox.showinfo(message="Password added successfully!")

    # Save updated data back to the file
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    # Clear the input fields after saving
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    target_website = website_entry.get()
    try:
        # Load existing data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # If the file is not found, show an error
        messagebox.showerror(message="No data file found.")
    except json.JSONDecodeError:
        # If the file is corrupted, ask if the user wants to clear it
        proceed = messagebox.askokcancel(
            message="The password file seems to be corrupted. Do you want to clear its contents?"
        )
        if proceed:
            with open("data.json", "w") as data_file:
                json.dump({}, data_file, indent=4)
            messagebox.showinfo(message="The file has been cleared.")
    else:
        # Search for the entered website in the data
        if target_website in data:
            email = data[target_website]["email"]
            password = data[target_website]["password"]
            messagebox.showinfo(title=target_website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showerror(message="No details for the website found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Entry
website_title = Label(text="Website:")
website_title.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Search Button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

# Email Entry
email_title = Label(text="Email/Username:")
email_title.grid(column=0, row=2)

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "aaqil@example.com")

# Password Entry
password_title = Label(text="Password:")
password_title.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
