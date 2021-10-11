import turtle
import random
import tqdm


def setup(myTurtle, myWin):
    myWin.reset()
    myWin.setup(1000, 1000)
    myTurtle.reset()
    myTurtle.speed('fastest')
    myTurtle.penup()
    myTurtle.goto(0, -300)
    myTurtle.left(90)
    myTurtle.pendown()


def drawBranch(maxDepth, distance, decrease, myTurtle, bar, index=0, angle=20):
    if index < maxDepth:
        coords = [myTurtle.xcor(), myTurtle.ycor()]
        # squigglyline(int(distance), 2, myTurtle)
        myTurtle.forward(distance)
        bar.update(1)
        for i in range(2):
            if i == 1:
                angle = -angle
            myTurtle.left(angle)
            drawBranch(maxDepth, distance * decrease, decrease, myTurtle, bar, index + 1)
            myTurtle.right(angle)
        myTurtle.penup()
        myTurtle.goto(coords[0], coords[1])
        myTurtle.pendown()


def squigglyline(length, squigglyness, t):
    for i in range(length // 2):
        angle = (random.random() * 2 - 1) * squigglyness
        t.forward(2)
        t.right(angle)


def main():
    bar = tqdm.tqdm(desc="fractal tree completion", total=2**10-1)
    bar.colour = 'green'
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    setup(myTurtle, myWin)
    drawBranch(10, 150, 0.8, myTurtle, bar)
    myWin.exitonclick()


if __name__ == "__main__":
    main()
