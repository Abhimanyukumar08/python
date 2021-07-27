import tkinter
from tkinter import *

win =Tk()

def nothing():
    file =Toplevel(win)
    button = Button(win,text='do nothing')
    button.pack()

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label='New Window',command=nothing)
filemenu.add_command(label='Open File',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Save',command=nothing)
filemenu.add_command(label='Save As',command=nothing)
filemenu.add_command(label='Close ',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Delete',command=nothing)
filemenu.add_command(label='Split',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=win.quit)

menubar.add_cascade(label='File',menu=filemenu)



win.config(menu=menubar)

win.mainloop()
