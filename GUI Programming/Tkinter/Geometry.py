import tkinter
from tkinter import *

win =Tk()

# pack method we have already done 

#grid method

# b=0
# for i in range(6):
#     for j in range(6):
#         b +=1
#         Button(win,text=str(b),borderwidth=1,).grid(row=i,column=j)



#place method
l1 = Label(win,text='Math')
l1.place(x=10,y=10)
e1=Entry(win,bd=5)
e1.place(x=60,y=10)
l2 = Label(win,text='English')
l2.place(x=10,y=60)
e2=Entry(win,bd=5)
e2.place(x=60,y=60)

b=Button(win,text='Submit')
b.place(x=100,y=100)



win.mainloop()
