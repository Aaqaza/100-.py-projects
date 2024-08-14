import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# Ask the user to enter a state until all states are guessed
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name?").title()

    # To stop if "Exit" is entered and save all remaining states in "states_to_learn.csv"
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # OR using file manipulation
    #
    # if answer_state == "Exit":
    #     with open("states_to_learn.csv", mode='w') as data:
    #         for state in all_states:
    #             if state not in guessed_states:
    #                 data.write(state + "\n")
    #     break

    # If answer guessed correctly
    if answer_state in all_states:
        guessed_states.append(answer_state)

        # Create turtle to write the name of state at the coords
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
