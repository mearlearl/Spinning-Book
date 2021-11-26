import tkinter as tk
import time
import numpy as np

from EulerSolve import get_angles
from Point import Point as p
from Point import Line as L

# Instatiate a Tk() object

frame = tk.Tk()
frame.title("Spinning Book")
frame.geometry('500x500')
frame.resizable(width=0, height=0)

# Create a Canvas object (it's like JPanel)

canvas = tk.Canvas(frame,width=500, height=500, borderwidth=0, highlightthickness=0,bg="#0000ff")
canvas.grid()

# I can add points and stuff here

distance = 1
theta1,theta2,theta3 = 0,0,0
angles = [theta3,theta2,theta1]

eulerangs = get_angles()

p1 = p(3*0.127,3*0.102,3*0.013)
p2 = p(3*0.127,3*0.102,-3*0.013)
p3 = p(3*0.127,-3*0.102,-3*0.013)
p4 = p(3*0.127,-3*0.102,3*0.013)
n1 = p(-3*0.127,3*0.102,3*0.013)
n2 = p(-3*0.127,3*0.102,-3*0.013)
n3 = p(-3*0.127,-3*0.102,-3*0.013)
n4 = p(-3*0.127,-3*0.102,3*0.013)

stuff = [L(p1,p2),L(p2,p3),L(p3,p4),L(p4,p1),L(n1,n2),L(n2,n3),L(n3,n4),L(n4,n1),L(p1,n1),L(p2,n2),L(p3,n3),L(p4,n4)]

def animateCanvas(e):
    
    angles = [0,0,0]

    for index in range(0,300):

        angels = [eulerangs[1][index],eulerangs[0][index], eulerangs[2][index]]

        angles[0] = angles[0] + angels[0]
        angles[1] = angles[1] + angels[1]
        angles[2] = angles[2] + angels[2]


        for drawthing in stuff:
            drawthing.update(distance,angles)
            drawthing.draw(canvas)

        frame.update()
        time.sleep(0.0333)
        canvas.delete("all")
        
    return

# This actually creates the Tk() object with all trimmings
frame.bind("<KeyRelease>", animateCanvas)
frame.mainloop()



