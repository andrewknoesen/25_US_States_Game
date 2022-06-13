import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guess the State", "What's another states name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        pandas.DataFrame(missing_states).to_csv("Missing_States.csv")
        break

    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_turtle.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        answer_turtle.write(answer_state, align="center")

