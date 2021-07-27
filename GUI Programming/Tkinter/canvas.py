import tkinter
from tkinter import *

win = Tk()

#creating canvas
c = Canvas(win,height=250,width=300,bg='blue')

#creating arc in the canvas, that is something like adding another window into other
coord = 10,35,240,210
arc = c.create_arc(coord,start=0, extent = 150,fill='red')
#line
line = c.create_line(15,15,200,200,fill='black')

c.pack()
win.mainloop()