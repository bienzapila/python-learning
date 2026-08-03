import random as rnd
import turtle as t
window = t.Screen()
t.speed(10)
def snowflake(length):
    for _ in range(8):
        for _ in range(3):
            t.forward(length/4)
            t.left(45)
            t.forward(length/4)
            t.backward(length/4)
            t.right(90)
            t.forward(length/4)
            t.backward(length/4)
            t.left(45)
        t.forward(length/4)
        t.backward(length)
        t.left(360/8)

for _ in range(rnd.randrange(1, 30)):
    t.penup()
    t.goto(rnd.randrange(0, 641), rnd.randrange(0, 481))
    t.pendown()
    snowflake(rnd.randrange(50, 200))


window.mainloop()