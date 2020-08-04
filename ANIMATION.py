__author__ = 'zakariya masood and hamza masood'

# please do not mess with this part unless you change the code significantly!#
import turtle
from tkinter import mainloop
import time

t = turtle.Pen()

DEFAULTPENTURTLE = t.pencolor("Blue"), t.fillcolor("Red"), t.penup(), t.fd(-375), t.width(10), t.speed(1)

W = [t.pendown(), t.lt(90), t.fd(80), t.bk(80), t.lt(-90), t.fd(70), t.lt(90), t.fd(80), t.bk(80),
     t.lt(90), t.fd(35), t.lt(-90), t.fd(60)]

E = [t.penup(), t.bk(60), t.lt(-90), t.fd(70), t.pendown(), t.fd(80), t.bk(80), t.lt(90), t.fd(80), t.lt(-90),
     t.fd(80), t.lt(-90),
     t.fd(35), t.lt(-90), t.fd(80)]

L = [t.penup(), t.lt(90), t.fd(45), t.lt(90), t.fd(125), t.pendown(), t.fd(45), t.bk(45), t.lt(90), t.fd(80),
     t.bk(80), t.lt(-90), t.penup(),
     t.fd(80)]

C = [t.pendown(), t.fd(50), t.lt(180), t.fd(50), t.lt(-90), t.fd(80), t.lt(-90), t.fd(50), t.penup(), t.fd(50)]

O = [t.pendown(), t.fd(50), t.lt(-90), t.fd(80), t.lt(-90), t.fd(50), t.lt(-90), t.fd(10), t.penup(), t.fd(10),
     t.pendown(), t.fd(10), t.penup(), t.fd(10),
     t.pendown(), t.fd(10), t.penup(), t.fd(10), t.pendown(), t.fd(10), t.penup(), t.fd(10)]

M = [t.lt(-90), t.penup(), t.fd(100), t.pendown(), t.fd(80), t.bk(80), t.lt(-90), t.fd(80), t.bk(80),
     t.lt(90), t.fd(45),
     t.lt(-90), t.fd(80), t.bk(80), t.lt(90), t.fd(45), t.lt(-90), t.fd(80), t.bk(80), t.lt(90), t.penup(),
     t.lt(-90), t.fd(80)]

E = [t.lt(90), t.fd(50), t.pendown(), t.fd(80), t.lt(180), t.fd(80), t.lt(-90), t.fd(80), t.lt(-90), t.fd(80),
     t.lt(-90), t.fd(35), t.lt(-90), t.fd(80)]

mainloop()
