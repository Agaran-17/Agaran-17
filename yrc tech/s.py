import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Animated YRC with Pattern Background")
screen.bgcolor("black")
screen.setup(width=800, height=800)

# Create the turtle for drawing the background pattern
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)  # Fastest speed
pattern_turtle.width(2)
pattern_turtle.hideturtle()

# Function to draw an animated, colorful spiral pattern
def draw_rotating_pattern():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
    for i in range(36):
        pattern_turtle.color(random.choice(colors))
        pattern_turtle.forward(i * 5)
        pattern_turtle.right(91)  # Unique angle for a dynamic spiral effect

# Create the turtle for drawing the "YRC" text
text_turtle = turtle.Turtle()
text_turtle.color("white")
text_turtle.speed(1)
text_turtle.width(5)
text_turtle.hideturtle()

# Function to animate the letter "Y"
def draw_Y():
    text_turtle.penup()
    text_turtle.goto(-80, 50)
    text_turtle.setheading(60)
    text_turtle.pendown()
    text_turtle.forward(60)
    time.sleep(0.5)
    text_turtle.backward(60)
    text_turtle.setheading(-60)
    text_turtle.forward(60)

# Function to animate the letter "R"
def draw_R():
    text_turtle.penup()
    text_turtle.goto(0, 50)
    text_turtle.setheading(90)
    text_turtle.pendown()
    text_turtle.forward(60)
    time.sleep(0.5)
    text_turtle.right(90)
    text_turtle.circle(-20, 180)
    text_turtle.setheading(-45)
    text_turtle.forward(40)

# Function to animate the letter "C"
def draw_C():
    text_turtle.penup()
    text_turtle.goto(80, 50)
    text_turtle.setheading(180)
    text_turtle.pendown()
    text_turtle.circle(30, 180)

# Main animation loop
for _ in range(36):
    draw_rotating_pattern()  # Draw the background pattern
    pattern_turtle.right(10)  # Rotate for animation effect
    screen.update()  # Update the screen to see the rotation effect

# Draw each letter with animation
draw_Y()
draw_R()
draw_C()

# Complete
turtle.done()


