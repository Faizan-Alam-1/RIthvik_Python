import turtle

screen = turtle.Screen()

t = turtle.Turtle()
t.color("Red")

for _ in range(10):
    t.forward(100)
    t.right(144)


screen.exitonclick()
