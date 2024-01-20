import turtle
import pandas
from time import sleep
import winsound
screen = turtle.Screen()
screen.title('US State Game')

image = 'blank_states_img.gif'
screen.addshape(image)

US_Map = turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = (data['state'])
states = states.to_list()

guessed_states = []
number_of_states_guessed = len(guessed_states)

clear = []


def start():
    nongs = pandas.read_csv('Data_Save.csv')
    if nongs.empty != True:
        non_guessed_states = nongs['0']
        non_guessed_states = non_guessed_states.to_list()
        for state in states:
            if state not in non_guessed_states:
                guessed_states.append(state)
                guess_x = (data[data.state == f'{state}'])
                guess_x = int(guess_x.x)
                guess_y = (data[data.state == f'{state}'])
                guess_y = int(guess_y.y)
                state_label = turtle.Turtle()
                state_label.penup()
                state_label.color('black')
                state_label.hideturtle()
                state_label.goto(x=guess_x, y=guess_y)
                state_label.write(f"{state}", font=('style', 10), align='center')


start()
while number_of_states_guessed != 50:
    guess = screen.textinput(title=f'{len(guessed_states)}/50 states guessed', prompt='Type your next guess').lower()
    if guess == 'exit':
        stateslf = []
        for state in states:
            if state not in guessed_states:
                stateslf.append(state)
        guessed_data = pandas.DataFrame(stateslf)
        guessed_data = guessed_data.to_csv("Data_Save.csv")
        break

    if guess == 'clear':
        guessed_data = pandas.DataFrame(clear)
        guessed_data = guessed_data.to_csv("Data_Save.csv")
        break

    elif guess in states and guess not in guessed_states:
        print(f'{guess} is correct')
        guessed_states.append(guess)
        guess_x = (data[data.state == f'{guess}'])
        guess_x = int(guess_x.x)
        guess_y = (data[data.state == f'{guess}'])
        guess_y = int(guess_y.y)
        print(guess_x, guess_y)
        state_label = turtle.Turtle()
        state_label.penup()
        state_label.color('red')
        state_label.hideturtle()
        state_label.goto(x=guess_x, y=guess_y)
        state_label.write(f"{guess}", font=('style', 10), align='center')
        for loop in range(0, 3):
            state_label.clear()
            sleep(.2)
            if loop == 2:
                state_label.color('black')
            state_label.write(f"{guess}", font=('style', 10), align='center')
            winsound.Beep(frequency=1500, duration=2 )
            sleep(.2)

        print(guessed_states)

    elif guess in states and guess in guessed_states:
        continue

    elif guess not in states:
        continue

    if len(guessed_states) == 50:
        screen.clear()
        win_screen = turtle.Turtle()
        win_screen.write(f"You have guessed all 50 states, congrats", font=('style', 30), align = 'center')


