import turtle
import pandas as pd
data = pd.read_csv("50_states.csv")
scr = turtle.Screen()
scr.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()
state_turtle.speed(10)


def match_the_name(name_of_the_state):
    state_turtle.goto(data[data["state"] == name_of_the_state].x.values[0],
                      data[data["state"] == name_of_the_state].y.values[0])
    state_turtle.write(name_of_the_state, True, "center", ("Courier", 10, "normal"))


def creat_csv(states):
    dic = {"state": [], "x": [], "y": []}
    for state in data["state"].values:
        if state not in states:
            state.title()
            dic["state"].append(state)
            dic["x"].append(data[data["state"] == state].x.values[0])
            dic["y"].append(data[data["state"] == state].y.values[0])
    ex_data = pd.DataFrame(dic)
    ex_data.to_csv("ex_data.csv")


quiz_finished = False
score = 0
answers = []
while not quiz_finished:
    if score == 50:
        quiz_finished = True

    else:
        answer = turtle.textinput(title=f"{score}/50 is your score", prompt="Give a state name?")

    if answer.title() in data["state"].values:
        answers.append(answer.title())
        score += 1
        match_the_name(answer.title())
    elif answer.title() == "Exit":
        creat_csv(answers)
        break
    else:
        pass


scr.exitonclick()
