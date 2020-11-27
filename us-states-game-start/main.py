import pandas
from turtle import Turtle, Screen

screen = Screen()
words = Turtle()
turtle = Turtle()
words.color("red")
words.hideturtle()
screen.setup(width=730, height=500)
screen.bgcolor("black")
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
########################################
# Code to get the x and y values of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#########################################
# Constants for words
COLOR = "red"
FONT = ("System", 10, "normal")
ALIGN = "center"

data = pandas.read_csv("50_states.csv")
raw_state = data["state"].tolist()
state = [item.lower() for item in raw_state]
save_state = state
correct_answer = 0
game_on = True
while game_on:
    num_of_states = len(state)
    user_input = screen.textinput(title=f"{correct_answer}/50", prompt="Name a state:").lower()
    print(user_input)
    answer = user_input.capitalize()

    if user_input in state:
        row_data = data[data.state == f"{answer}"]
        print(row_data)
        x_value = int(row_data.x)
        y_value = int(row_data.y)
        words.penup()
        words.goto(x_value, y_value)
        words.write(f"{answer}", font=FONT, align=ALIGN)
        correct_answer += 1
        save_state.remove(user_input)
    if user_input == "exit":
        df = pandas.DataFrame(save_state)
        df.to_csv("states_to_learn.csv")
        break

    # if correct_answer == 50:
    #     words.write("GAME OVER\nYou got them all!", font=("System", 20, "bold"), align=ALIGN)
    #     game_on = False

