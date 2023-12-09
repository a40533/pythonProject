from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    for seg in range(2, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)


screen.exitonclick()
