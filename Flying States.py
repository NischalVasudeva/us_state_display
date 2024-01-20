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

for guess in states:
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
    state_label.write(f"{guess}", font=('style', 10), align='center', move=True)
    state_label.goto(x=guess_x, y=guess_y)
    for loop in range(0, 3):
                state_label.clear()
                sleep(.2)
                if loop == 2:
                    state_label.color('black')
                state_label.write(f"{guess}", font=('style', 10), align='center',)
                winsound.PlaySound('hey', winsound.SND_FILENAME)
                sleep(.2)


        #     print(guessed_states)
        #
        # if guess in states and guess in guessed_states:
        #     print('You already guessed this state')
        #     guess = screen.textinput(title=f'{len(guessed_states)}/50 states guessed', prompt='Type your next guess')
        #
        # if guess not in states:
        #     print("try again")
        #     guess = screen.textinput(title=f'{len(guessed_states)}/50 states guessed', prompt='Type your next guess')
        #

turtle.mainloop()
