from turtle import Turtle, Screen
import random
is_race_on= True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles=[]


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on= True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the {winning_color} is winner")
            else:
                print(f"you lost the winner is {winning_color}")

        rand_distance = random.randint(8,10)
        turtle.forward(rand_distance)

screen.exitonclick()