import turtle

tt=turtle.Turtle()
tt.pencolor("red")

tt.speed(0)
tt.penup()
tt.goto(0,200)
tt.pendown()

h = 0
r = 0

while(True):
    tt.forward(h)
    tt.right(r)
    h += 3
    r += 1
    if r == 220:
        break
    tt.hideturtle()

turtle.done()