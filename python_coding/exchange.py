from tkinter import *

w = Tk()

def ttt():
    r =round((float(e1.get()) / 1438.5 ), 2)
    msg["text"] = str(r) + "달러"
    msg["fg"] = "red"

Label(w, text="한화").grid(row=0, column=0)
e1  = Entry(w)
e1.grid(row=0, column=1)
Button(w, text="환전하기", command=ttt).grid(row=1, column=0)

msg = Label(w, text="0달러")
msg.grid(row=1, column=1)
w.mainloop()