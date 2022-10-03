# from tkinter import mainloop
# import turtle
# turtle.forward(50)
# turtle.right(9)
# turtle.forward(50)
# turtle.mainloop()

from turtle import *

RawTurtle
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()