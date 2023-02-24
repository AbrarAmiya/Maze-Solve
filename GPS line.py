
import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Define the maze as a 2D array of 1s and 0s
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Set up the turtle for drawing
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()

# Draw the maze using lines
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 1:
            turtle.forward(50)
        else:
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()
    turtle.penup()
    turtle.goto(-250, 250 - 50 * (i + 1))
    turtle.pendown()

# Set up the car turtle
car = turtle.Turtle()
car.shape('turtle')
car.color('red')
car.penup()
goal = turtle.Turtle()
goal.shape('ball')
goal.color('blue')
goal.penup()
# Set the car's initial position to the start of the maze
start_x, start_y = -225, 225
car.goto(start_x, start_y)

# Set the goal point
goal_x, goal_y = -40, -100

# Define a function to check if a position is clear of lines
def is_clear(x, y):
    if (x < -250 or x > 250 or y < -250 or y > 250):
        return False
    if (x, y) == (goal_x, goal_y):
        return True
    car.penup()
    car.goto(x, y)
    overlaps = car.overlapping(-250, -250, 500, 500)
    car.goto(start_x, start_y)
    return not overlaps

# Define a function to move the car to the goal while avoiding lines
def move_to_goal():
    while (car.xcor(), car.ycor()) != (goal_x, goal_y):
        x, y = car.position()
        dx, dy = goal_x - x, goal_y - y
        # Calculate the next position along the path to the goal
        if abs(dx) > abs(dy):
            next_x = x + 50 if dx > 0 else x - 50
            next_y = y + dy * 50 // abs(dx)
        else:
            next_x = x + dx * 50 // abs(dy)
            next_y = y + 50 if dy > 0 else y - 50
        # Check if the next position is clear of lines
        if is_clear(next_x, next_y):
            car.goto(next_x, next_y)
            
# Call the function to move
move_to_goal()

# Exit the screen when the user
screen.exitonclick()