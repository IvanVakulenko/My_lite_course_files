from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()

main.title('The Digital Clock in Python')

def clock() :
    tick = strftime('%H:%M:%S: %p')

    clock.label .config(text = tick)
    clock.label .after(1000, clock)

clock.label = Label(main, font = ('sans', 80), background = 'blue', foreground = 'white')

clock.label.pack(anchor = 'center')

clock()
mainloop()