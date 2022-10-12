import math
import turtle


ls = 100 #letterside
s_d = math.sqrt(ls*ls+0.5*ls*0.5*ls) #short_diagonal
l_d = math.sqrt(4*ls*ls+ls*ls) #long diagonal
sine = math.sin(0)

turtle.speed(1)

turtle.right(-90)
turtle.forward(ls)
turtle.right(45+22.5)
turtle.forward(s_d)
turtle.right(45)
turtle.forward(s_d)
turtle.right(90+45+22.5)
turtle.forward(ls*2)
turtle.right(-90-45-22.5)
turtle.forward(s_d*2)
turtle.right(90+45+22.5)
turtle.forward(ls*2)
turtle.right(90+45+22.5)
turtle.forward(s_d*2)
turtle.right(90+22.5)
turtle.forward(ls)






turtle.mainloop()