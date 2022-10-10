import turtle


def n_polygon(sidor, sidlängd):
    antal_grader = 360 / sidor
    for x in range(sidor):
        turtle.forward(sidlängd)
        turtle.right(antal_grader)



for x in range(1, 10):
    n_polygon(x, 50)

turtle.mainloop()