# from tkinter import mainloop
from tkinter import E
from turtle import *

counter = 10.0
color_value = 0
while(True):
    right(10)
    forward(counter)
    counter += 0.1
    color_value += 0.1
    if(color_value > 1):
        color_value = 0
    if(int(counter) % 3 == 0):
        color(color_value, 1, 1)
    elif(int(counter) % 3 == 1):
        color(1, color_value, 1)
    else:
        color(1, 1, color_value)
    # color(color_value, color_value, color_value)