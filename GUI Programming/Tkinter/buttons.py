import tkinter
from tkinter import *

win =Tk()

#creating check button
c1=IntVar()  #this is store the value of the check button 
c2= IntVar()
cb =Checkbutton(win,text='Music',offvalue=0,onvalue=1,height=5,width=5,variable=c1)
cb2 =Checkbutton(win,text='Video',offvalue=0,onvalue=1,height=5,width=5,variable=c2)
cb.pack()
cb2.pack()

#creatinga radio button
var = IntVar()
r1= Radiobutton(win,text='option 1',value=1)
r1.pack()
r2= Radiobutton(win,text='option 2',value=2)
r2.pack()
r3= Radiobutton(win,text='option 3',value=3)
r3.pack()
r4= Radiobutton(win,text='option 4',value=4)
r4.pack()


win.mainloop()
