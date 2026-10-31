import turtle
t = turtle.Turtle()

t.penup()
def line(l, x, y):
    t.goto(x, y)
    t.pendown()
    t.forward(l)
    t.penup()
    if l > 30: 
        line(l/2, x + 20, y + 20)
        line(l/2, x - 21, y - 21)


line(100, 0 , 0)


def count(n): 
    if n > 0: 
        print(n)
        count(n-1)
    






#turtle.mainloop()

