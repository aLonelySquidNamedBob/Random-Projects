import turtle
import time

t1 = turtle.Turtle()
t1.speed('fastest')
t2 = turtle.Turtle()
t2.speed('fastest')

start = time.time()
t1.forward(100)
elapsed = time.time() - start
print(elapsed)

start = time.time()
t2.goto(100, 0)
elapsed = time.time() - start
print(elapsed)
