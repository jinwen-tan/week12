from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')
    

window = Tk(className= "Tkinter example 1")
window1 = Tk(className= "Tkinter example 2")

button = Button(window,text='press', command=reply)
button1 = Button(window1,text='test', command=reply)

button.pack()
button1.pack()

window.geometry("200x200")
window1.geometry("300x200")

window.mainloop()
window1.mainloop()

