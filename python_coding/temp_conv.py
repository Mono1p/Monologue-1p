#온도 변환 프로그램

from tkinter import *

def CCC():
    r = (float(e1.get()) - 32) * 5/9
    e2.delete(0, END)
    e2.insert(0, r)

def FFF():
    r = (float(e2.get()) * 9/5) + 32
    e1.delete(0, END)
    e1.insert(0, r)

def clear():
    e1.delete(0, END)
    e2.delete(0, END)

w = Tk()
Label(w, text="화씨").grid(row=0, column=0)
e1 = Entry(w)
e1.grid(row=0, column=1)

Label(w, text="섭씨").grid(row=1, column=0)
e2 = Entry(w)
e2.grid(row=1, column=1)

f =Frame(w)
Button(f, text="화씨->섭씨", command=CCC).pack(side=LEFT)
Button(f, text="섭씨->화씨", command=FFF).pack(side=LEFT)
Button(f, text="초기화", command=clear).pack(side=LEFT)
f.grid(row=2, column=0, columnspan=2)

w.mainloop()
