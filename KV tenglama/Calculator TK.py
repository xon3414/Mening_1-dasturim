from tkinter import *
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.geometry('250x400')
window["bg"]="lightgreen"

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(window, style='lefttab.TNotebook')
notebook1 = ttk.Notebook(window, style='lefttab.TNotebook')
f1 = tk.Frame(notebook)
f2 = tk.Frame(notebook1, bg='blue', width=200, height=200)
notebook.add(f1, text='Frame 1')
notebook1.add(f2, text='Frame 2')
notebook.pack()

lbl = Label(notebook, text="axx+bx+c=0")
lbl.grid(column=3, row=0, columnspan=5)
lbl = Label(notebook, text="xx+")
lbl.grid(column=2, row=1, sticky=W)
lbl = Label(notebook, text="x+")
lbl.grid(column=4, row=1, sticky=W)
lbl = Label(notebook, text="=0")
lbl.grid(column=6, row=1, sticky=W)
lbl = Label(notebook, text="D=")
lbl.grid(column=0, row=2)
lbl = Label(notebook, text="X1=")
lbl.grid(column=0, row=3)
lbl = Label(notebook, text="X2=")
lbl.grid(column=0, row=4)
lbl1 = Label(notebook, text=" ")
lbl1.grid(column=1, row=2, columnspan=5, sticky=W)
lbl2 = Label(notebook, text=" ")
lbl2.grid(column=1, row=3, columnspan=5, sticky=W)
lbl3 = Label(notebook, text=" ")
lbl3.grid(column=1, row=4, columnspan=5, sticky=W)
lbl4 = Label(notebook, text=" ")
lbl4.grid(column=1, row=5, columnspan=5, sticky=W)
lbl5 = Label(notebook, text=" ")
lbl5.grid(column=1, row=6, columnspan=5, sticky=W)

a = Entry(notebook, width=3)
a.grid(column=1, row=1, sticky=W)
b = Entry(notebook, width=3)
b.grid(column=3, row=1, sticky=W)
c = Entry(notebook, width=3)
c.grid(column=5, row=1, sticky=W)

def clicked():

    D = int(b.get())**2 - 4*int(a.get())*int(c.get())
    lbl1.configure(text=D)
    if D>0:
        X1 = (int(b.get())*-1 + D**(1/2))/(2*int(a.get()))
        X2 = (int(b.get())*-1 - D**(1/2))/(2*int(a.get()))
        lbl2.configure(text=X1)
        lbl3.configure(text=X2)
    elif D==0:
        X = int(b.get())*-1/(2*int(a.get()))
        lbl4.configure(text=X)
    else:
        N=text="There is no answer"
        lbl5.configure(text=N)

btn = Button(notebook, text="get", command=clicked, bg="lightgreen")
btn.grid(column=0, row=7)

window.mainloop()
