from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    answer = round(miles * 1.609, 2)
    km.config(text=answer)


window = Tk()
window.title("Mile to km converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.insert(END, string="0")
miles_input.grid(column=2, row=1)

miles_txt = Label(text="Miles")
miles_txt.grid(column=3, row=1)

equal_txt = Label(text="is equal to")
equal_txt.grid(column=1, row=2)

km = Label(text="0")
km.grid(column=2, row=2)

km_txt = Label(text="Km")
km_txt.grid(column=3, row=2)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=2, row=3)

window.mainloop()
