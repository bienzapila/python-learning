import turtle as t
window = t.Screen()

t.pensize(10)
list_info = [('blue', 0, 0), ('black', 100, 0), ('red', 200, 0), ('yellow', 50, -75), ('green', 150, -75)]
for info in list_info:
    t.penup()
    t.goto(info[1], info[2])
    t.color(info[0])
    t.pendown()
    t.circle(50)

window.mainloop()