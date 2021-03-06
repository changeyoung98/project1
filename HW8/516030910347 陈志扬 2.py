# File: five_mouse-click.py
# A program that allows the user to draw a simple house using five mouse-clicks
# By: Daisy
from graphics import *
def main():
    win=GraphWin("House",640,480)
    t1=Text(Point(320,10),'Two clicks for the opposite corners of the frame of the house')
    t1.draw(win)
    t2=Text(Point(320,25),'(lower-left and upper-right)')
    t2.draw(win)
    p1=win.getMouse()
    p1.draw(win)
    x1=p1.getX()
    y1=p1.getY()
    p2=win.getMouse()
    x2,y2=p2.getX(),p2.getY()
    p2.draw(win)
    Rectangle(p1,p2).draw(win)
    t1.undraw()
    t2.undraw()
    t3=Text(Point(320,10),'Click for the center of the top edge of a rectangular door')
    t3.draw(win)
    p3=win.getMouse()
    x3=p3.getX()
    y3=p3.getY()
    a=(x3-x1)/2
    Rectangle(Point(x3-a,y3),Point(x3+a,y1)).draw(win)
    t3.undraw()
    t4=Text(Point(320,10),'Click for the center of a square window')
    t4.draw(win)
    p4=win.getMouse()
    x4,y4=p4.getX(),p4.getY()
    b=a/2
    Rectangle(Point(x4-b,y4-b),Point(x4+b,y4+b)).draw(win)
    t4.undraw()
    t5=Text(Point(320,10),'Click for the peak of the roof')
    t5.draw(win)
    p5=win.getMouse()
    t5.undraw()
    Polygon(p5,p2,Point(x1,y2)).draw(win)
    Text(Point(600,10),'Click to quit').draw(win)
    win.getMouse()
    win.close()

main()
