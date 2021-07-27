
import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()

# frame = Frame(win)
# frame.pack(side=LEFT)
# rb = Button(frame,text='Red',fg='red')
# rb.pack(side=LEFT)
# bb=Button(frame,text='Blue',fg='blue')
# bb.pack()
# gg = Button(frame,text='Green',fg='green')
# gg.pack(side=LEFT)

# frame2 =Frame(win)
# frame2.pack(side=BOTTOM)
# bl =Button(frame2,text='Black',fg='black')
# bl.pack(side=BOTTOM)

#creating list box

# lb = Listbox(win)
# lb.insert(1,'python')
# lb.insert(2,'Java')
# lb.insert(3,'HTML')
# lb.insert(4,'CSS')
# lb.insert(5,'JavaScript')
# lb.pack()

# win.title('first')
# top = Toplevel()
# top.title('second')


#message box
def msg():
    messagebox.showinfo('from computer','Hi There!')

b=Button(win,text='Popup',command=msg)
b.pack()

win.mainloop()