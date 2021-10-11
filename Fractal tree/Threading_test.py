import turtle
import threading
import random


def squigglyline(length, squigglyness, t):
    for i in range(length // 2):
        angle = (random.random() * 2 - 1) * squigglyness
        t.forward(2)
        t.right(angle)


def setup(t, length):
    # t.hideturtle()
    t.speed('fastest')
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.forward(length)


def drawbranch(index, maxdepth, length, decrease, angle, t):
    if index < maxdepth:
        coords = [t.xcor(), t.ycor()]
        # t.forward(length)
        squigglyline(int(length), 2, t)
        t.left(angle)
        drawbranch(index + 1, maxdepth, length * decrease, decrease, angle, t)
        t.right(2 * angle)
        drawbranch(index + 1, maxdepth, length * decrease, decrease, angle, t)
        t.left(angle)
        # t.backward(length)
        t.penup()
        t.goto(coords[0], coords[1])
        t.pendown()


if __name__ == "__main__":

    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    setup(t1, 150)
    setup(t2, 150)
    t1.right(20)
    t2.left(20)

    thread1 = threading.Thread(target=drawbranch, args=(0, 5, 150 * 0.8, 0.8, 20, t1))
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=drawbranch, args=(0, 5, 150 * 0.8, 0.8, 20, t2))
    thread2.daemon = True
    thread2.start()

    turtle.Screen().exitonclick()

