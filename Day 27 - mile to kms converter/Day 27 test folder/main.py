from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("Day 27")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

button = Button(text="New button", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Brand new button")
new_button.grid(column=3, row=0)

input = Entry(width=10)
input.grid(column=4, row=3)






window.mainloop()
