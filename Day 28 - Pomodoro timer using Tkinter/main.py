from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND = "#ECFFE6"
RED = "#FF4E88"
GREEN = "#399918"
PINK = "#FF8A8A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=BACKGROUND)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="", font=(FONT_NAME, 50), fg=RED, bg=BACKGROUND)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # For testing
    # work_sec = 5
    # short_break_sec = 2
    # long_break_sec = 10

    if reps in (1, 3, 5, 7):
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
    elif reps in (2, 4, 6):
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)


# OR
# if reps % 8 == 0:
#     count_down(long_break_sec)
#     title.config(text="Break", fg=RED)
# elif reps % 2 == 0:
#     count_down(short_break_sec)
#     title.config(text="Break", fg=PINK)
# else:
#     count_down(work_sec)
#     title.config(text="Work", fg=GREEN)

# ---------------------------- WINDOW POP UP MECHANISM ------------------------------- #

def bring_window_to_front():
    window.lift()  # Bring the window to the top
    window.attributes("-topmost", True)  # Keep it above all other windows

    # Bind the FocusIn and FocusOut events to handle window focus changes
    window.bind("<FocusOut>", on_focus_out)
    window.bind("<FocusIn>", on_focus_in)


def on_focus_out(event):
    window.attributes("-topmost", False)  # Reset the topmost attribute when focus is lost


def on_focus_in(event):
    window.attributes("-topmost", True)  # Set the topmost attribute when the window gains focus

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = str(math.floor(count / 60)).zfill(2)
    count_sec = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            current_text = check_marks.cget("text")
            new_text = current_text + "☑︎"
            check_marks.config(text=new_text)
        bring_window_to_front()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKGROUND)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)

title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=BACKGROUND)
title.grid(column=2, row=1)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", bg=BACKGROUND, highlightbackground=BACKGROUND, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg=BACKGROUND, highlightbackground=BACKGROUND, command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(font=(FONT_NAME, 50), fg=RED, bg=BACKGROUND)
check_marks.grid(column=2, row=4)

window.mainloop()
