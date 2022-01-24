import turtle as T
import pandas as PD

# Set Screen up
screen = T.Screen()
screen.title("U.S States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
T.shape(image_path)

# Set Turtle up
writer = T.Turtle()
writer.hideturtle()
writer.penup()

# Read CSV Files
data = PD.read_csv("50_states.csv")
data = data.to_dict()

# Convert Data into List
state_list = []
for key in data:
    for item in data[key]:
        try:
            state_list[item].append(data[key][item])
        except IndexError:
            state_list.append([])
            state_list[item].append(data[key][item])

# Main
game_state = True
init_title = "Guess the state"
correct_guess = 0
total_states = len(state_list)
guessed_states = []

while game_state:
    user_input = screen.textinput(
        title=init_title, prompt="What's another state's name?").title()

    for state in state_list:
        if user_input in state:
            guessed_states.append(state)
            correct_guess += 1
            init_title = f"{correct_guess}/{total_states} States Correct"

            writer.goto(state[1], state[2])
            writer.write(arg=f"{user_input}", align="center",
                         font=('Courier', 10, 'italic'))

    if correct_guess == total_states:
        game_state = False

    if user_input == "Exit":
        missed_states = {
            "States to Learn": [state[0]
                                for state in state_list if state not in guessed_states]}

        PD.DataFrame(missed_states).to_csv("states_to_learn.csv")

        game_state = False

screen.mainloop()
