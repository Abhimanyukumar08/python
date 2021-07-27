import tkinter
from tkinter import *

win =Tk()

#scale
# s = Scale(win)
# s.pack() # it does not have any limit 

# #spinbox
# sb = Spinbox(win,from_=0,to=15) # we can set limit in this
# sb.pack()

#scrollbar
scrollbar = Scrollbar(win)

list = Listbox(win,yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT,fill=Y)
for line in range(100):
    list.insert(END,'This is line number '+str(line))
list.pack(side=LEFT,fill=BOTH)
scrollbar.config()

win.mainloop()