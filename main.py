# Event Handlers Code...
# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.exitonclick()

# Make A Sketch App...
# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(18)
#
#
# def move_backwards():
#     tim.backward(18)
#
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()

# Understanding Turtle Coordinate System By Building A Turtle Race Game...
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Enter The Color Of The Turtle Which Will Win The Race: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won The Game! Winner's Color Is: {winning_color}.")
            else:
                print(f"You Lost The Game! Winner's Color Is: {winning_color}.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
