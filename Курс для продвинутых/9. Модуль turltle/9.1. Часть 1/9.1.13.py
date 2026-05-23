import turtle as t

window = t.Screen()
t.right(90)
for i in range(100, 0, -1):
    t.forward(i)
    t.right(90)
window.mainloop()
