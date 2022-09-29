#이진수를 입력하면 십진수로 변환해주는 프로그램.

from tkinter import *

w = Tk()

def ttt():
    T = int(e1.get(), 2)
    e2.delete(0, END)
    e2.insert(0, T)

def qqq():
    Q = bin(int(e2.get()))
    e1.delete(0, END)
    e1.insert(0, Q)

Label(text="2진수").grid(row=0, column=0)
e1 = Entry(w)
e1.grid(row=0, column=1)

Label(text="10진수").grid(row=1, column=0)
e2 = Entry(w)
e2.grid(row=1, column=1)


f = Frame(w)
Button(f, text="2진수->10진수", command=ttt).pack(side=LEFT)
Button(f, text="2진수->10진수", command=qqq).pack(side=LEFT)
f.grid(row=2, column=0, columnspan=2)

w.mainloop()