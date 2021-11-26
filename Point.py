import math as m

class Point:

    def __init__(self, setx, sety, setz):

        self.x=setx
        self.y=sety
        self.z=setz
        self.px = 0
        self.py = 0
        self.size = 0

        return

    def draw(self,c):

        c.create_oval(self.px-self.size/2.0,self.py-self.size/2.0,self.px+self.size/2.0,self.py+self.size/2.0, fill = "red")

        return

    def update(self,d,ts):

        nx = m.cos(ts[0])*m.cos(ts[1])*self.x + (m.cos(ts[0])*m.sin(ts[1])*m.sin(ts[2]) - m.sin(ts[0])*m.cos(ts[2]))*self.y + (m.cos(ts[0])*m.sin(ts[1])*m.cos(ts[2]) + m.sin(ts[0])*m.sin(ts[2]))*self.z
        ny = m.sin(ts[0])*m.cos(ts[1])*self.x + (m.sin(ts[0])*m.sin(ts[1])*m.sin(ts[2]) + m.cos(ts[0])*m.cos(ts[2]))*self.y + (m.sin(ts[0])*m.sin(ts[1])*m.cos(ts[2]) - m.cos(ts[0])*m.sin(ts[2]))*self.z
        nz =             -m.sin(ts[1])*self.x                                            + m.cos(ts[1])*m.sin(ts[2])*self.y                                           +  m.cos(ts[1])*m.cos(ts[2])*self.z

        r = d-nx
        maxh = 1+r/4
        hpix = 432*nz/maxh
        sizepix = 40/(r**0.5)
        overpix = 432*ny/maxh

        self.px = 500/2 + overpix
        self.py = 500/2 - hpix
        self.size = sizepix


        return    

class Line:

    def __init__(self, pointA, pointB):

        self.p1 = pointA
        self.p2 = pointB

        return

    def update(self, d, ts):

        self.p1.update(d,ts)
        self.p2.update(d,ts)

        return
    
    def draw(self, c):

        c.create_line(self.p1.px,self.p1.py,self.p2.px,self.p2.py,width=2)

        return
