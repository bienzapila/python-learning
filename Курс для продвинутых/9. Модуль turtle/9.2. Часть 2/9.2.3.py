import turtle as t
window = t.Screen()

t.shape('triangle')
t.dot()
n = int(input())
for _ in range(n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.left(360 / n)


window.mainloop()