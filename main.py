import turtle
import pandas

"""
U.S. States Guessing Game

This game allows the user to guess U.S. states.
If the guess is correct, the state name is displayed on the map.
At the end, a CSV file with missed states is generated.
"""

# Load dataset with states and coordinates
df = pandas.read_csv("50_states.csv")

# Create a lowercase version of state names for easier comparison
df["state_lower"] = df["state"].str.lower()

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create pen for writing state names
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Convert columns to lists
state_column = df.state.to_list()
lower_state_column = df.state_lower.to_list()

guesses = []
score = 0

while len(guesses) < len(lower_state_column):
    """
    Main game loop:
    - Ask user for input
    - Check correctness
    - Display result
    """
    answer = screen.textinput(
        title=f"{score} / {len(lower_state_column)} Guess the state",
        prompt="What's another state's name?"
    )

    # Exit if user cancels input
    if answer is None:
        break

    answer_state = answer.lower().strip()

    if answer_state == "exit":
        break

    # Find matching state
    state_data = df[df.state_lower == answer_state]

    # If correct and not guessed before
    if not state_data.empty and answer_state not in guesses:
        score += 1

        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])

        pen.goto(x, y)
        pen.write(state_data.state.iloc[0])

        guesses.append(answer_state)

# Generate list of missed states
not_guessed = [
    state.title()
    for state in lower_state_column
    if state not in guesses
]

# Save to CSV
new_df = pandas.DataFrame({
    "States To Learn": not_guessed
})

new_df.to_csv("states_to_learn.csv", index=False)