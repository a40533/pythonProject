from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def move_clockwise():
    my_turtle.left(10)


def move_anticlockwise():
    my_turtle.right(10)


def clear():
    my_turtle.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="space", fun=clear)
screen.exitonclick()
