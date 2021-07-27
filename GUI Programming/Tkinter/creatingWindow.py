import tkinter
from tkinter import *

win = Tk()
win.geometry("500x500")
#ADDING WIDGETS IN THE WINDOW

#1.adding buttons
def pr():
    print('HEllO')
b1= Button(win,text='button 1',command=pr,padx=10,pady=10,activebackground='red')
# b1.grid(row=1,column=1)
b1.place(x=100,y=150)   #we can also use place instead of grid 
# b2 = Button(win,text='button 2')
# # b2.grid(row=1,column=2)
# b2.place(x=150,y=100)



win.mainloop()