import turtle

# Define the grammar rules 
grammar = {
    "F": "F+F-F-F+F",  # Rule 1
    "X": "F+X",       # Rule 2
    "Y": "X-Y"        # Rule 3
}

# Define the starting state
start = 'Y'

# Define the angle of rotation for the turtle
angle = 60

# Define the step size for the turtle
step_size = 5

# Define the number of iterations to run the grammar
num_iterations = 5

def generate_fractal(state, grammar, num_iterations):
    """Generate string after applying the grammar rules for the given number of iterations."""
    for i in range(num_iterations):
        new_state = ""
        for char in state:
            if char in grammar:
                new_state += grammar[char]
            else:
                new_state += char
        state = new_state
    return state

def draw_fractal(state, angle, step_size):
    """Draw fractal using turtle graphics."""
    for char in state:
        if char == "F":
            turtle.forward(step_size)
        elif char == "+":
            turtle.right(angle)
        elif char == "-":
            turtle.left(angle)

# Generate string using the given grammar and number of iterations
fractal_string = generate_fractal(start, grammar, num_iterations)

# Initialize the turtle
turtle.speed("fastest")
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

# Draw fractal using turtle graphics
for i in range(6):
    draw_fractal(fractal_string, angle, step_size)
    turtle.right(120)

# Keep the turtle window open
turtle.done()
