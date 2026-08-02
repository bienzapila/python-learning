import turtle as t
window = t.Screen()
colors = ['yellow', 'blue', 'red', 'orange', 'purple', 'green']
n_color = 0
pensize = 1
distance = 10
for _ in range(50):
    t.left(45)
    if n_color >= len(colors):
        n_color = 0
    t.pencolor(colors[n_color])
    n_color += 1
    t.pensize(pensize)
    pensize += 0.3
    t.forward(distance)
    distance += 2

window.mainloop()