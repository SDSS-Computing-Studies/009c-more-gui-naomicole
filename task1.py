#! python3

import math
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("tk")
win.geometry("500x350")
answer = StringVar()
answer.set("A = ")

def clickFunction():
    h = e4.get()
    a = e1.get()
    b = e2.get()
    c = e3.get()

    if a != "" and b != "" and c != "":
       
        a = int(a)
        b = int(b)
        c = int(c)

        s = (a+b+c)/2
        A = math.sqrt(s*(s-a)*(s-b)*(s-c))

        answer.set(A)

    elif h != "" and b != "" and a == "" and c == "":
        
        b = int(b)
        h = int(h)

        A = b*h/2

        answer.set(A)

    else:
        A = "the area cannot be calculated\nfrom the information given"
        answer.set(A)

triangle = PhotoImage(file="triangle.png")
l1 = Label(win,image=triangle)
l2 = Label(win,text="Enter as much information about the\ntriangle shown and I will calculate the area")
l3 = Label(win,textvariable=answer)
b1 = Button(win,text="Calculate!",command=clickFunction)
e1 = Entry(win,text="sidea",width=5)
e2 = Entry(win,text="base",width=5)
e3 = Entry(win,text="sidec",width=5)
e4 = Entry(win,text="height",width=5)

l1.place(x=0,y=0)
l2.place(x=0,y=275)
l3.place(x=325,y=280)
b1.place(x=250,y=280)
e1.place(x=180,y=100)
e2.place(x=225,y=225)
e3.place(x=400,y=135)
e4.place(x=310,y=125)


win.mainloop()