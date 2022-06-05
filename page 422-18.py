from tkinter import Tk, Canvas
from tkinter.ttk import Button,Frame


def press_blue():
    color = 'blue'
    if color=='blue':
        canvas.itemconfigure(yellow_lamp,fill='blue')
def press_green():
    color = 'green'
    if color=='green':
        canvas.itemconfigure(yellow_lamp,fill='green')

root=Tk()
root.title('traffic light')
frame = Frame(root)
frame.pack()
canvas = Canvas(frame , width=80,height=80)
green_lamp = canvas.create_oval(10,30,60,80,fill='blue')
button = Button(frame,text='On',command=press_green)
button2 = Button(frame,text='OFF',command=press_blue)
button.grid(row=0,column=0)
button2.grid(row=1,column=0)
canvas.grid(row=0,column=1)
root.mainloop()
