from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bets = []
user_names = []
no_of_users = screen.numinput(title="No of users", prompt="Enter no of players: ")

for n in range(int(no_of_users)):
    user_name = screen.textinput(title="Enter player name", prompt="What is your name?")
    user_names.append(user_name)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    user_bets.append(user_bet)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

y = -112
is_race_on = False

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y += 28
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)

if user_bets:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            winner_found = False  # Flag to track if a winner is found
            for i in range(len(user_bets)):
                if user_bets[i] == winning_color:
                    print(f"{user_names[i]} won. The {winning_color} turtle is the winner")
                    winner_found = True  # Set the flag to True
                    break  # Exit the loop once a winner is found
            if not winner_found:  # If no winner is found, print nobody won
                print(f"Nobody won. The {winning_color} turtle is the winner")
            break  # Exit the outer loop as well since race is over
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
