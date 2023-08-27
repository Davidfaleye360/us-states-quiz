import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
writing_turtle = turtle.Turtle()
writing_turtle.penup()
writing_turtle.hideturtle()

states_data = pandas.read_csv('50_states.csv')
states = states_data.state.to_list()

ans_list = []

while len(ans_list) < 50:
    answer = (screen.textinput(title=f'{len(ans_list)}/50 correct state', prompt='What is another state')).title()
    if answer == 'Exit':
        missed_states = [state for state in states if state not in ans_list]
        pandas.DataFrame(missed_states).to_csv('missed_states.csv')
        break

    if answer in states and answer not in ans_list:
        ans_list.append(answer)
        state_data = states_data[states_data.state == answer]
        writing_turtle.goto(int(state_data.x), int(state_data.y))
        writing_turtle.write(answer)





