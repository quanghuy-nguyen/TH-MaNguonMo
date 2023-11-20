# bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
# để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
import tkinter
from tkinter import  *
from tkinter.ttk import *

window = Tk()
window.geometry('450x600')
window.title("cua so chinh")

def hien_thi():
    n1 = int(n.get())

    A = np.zeros((n1, n1))
    B = np.zeros(n1)

    for i in range(n1):
        for j in range(n1):
            A[i][j] = float(entry_a[i][j].get())

    for i in range(n1):
        B[i] = float(entry_b[i].get())

    A1 = np.linalg.inv(A)

    print("A = ", A)
    print("B = ", B)
    print("A1 = ", A1)
    X = np.dot(A1, B)
    print(X)
    lb4.config(text=f"X = {X}")


def hien_thi1():
    n1 = int(n.get())
    for i in range(n1):
        row_coeffs = []
        for j in range(n1):
            label = Label(window, text=f"a{i + 1}{j + 1}:")
            label.grid(row=i + 3, column=j * 2)

            entry = Entry(window)
            entry.grid(row=i + 3, column=j * 2 + 1)
            row_coeffs.append(entry)
        entry_a.append(row_coeffs)

        label_b = Label(window, text=f"b{i + 1}:")
        label_b.grid(row=i + 3, column=n1 * 2)

        entry = Entry(window)
        entry.grid(row=i + 3, column=n1 * 2 + 1)
        entry_b.append(entry)
    return

n = StringVar()

txt1 = Entry(window, textvariable= n)
txt1.place(x=160, y= 370 )

btt1 = Button(window, text = "nhap lieu", command= hien_thi1)
btt1.place(x=160, y= 400 )
btt2 = Button(window, text = "tinh toan", command= hien_thi)
btt2.place(x=250, y= 400 )

lb1 = tkinter.Label(window, text = "nhap so pt va so an (n): ", fg = "green")
lb1.place(x=15, y= 370)

lb4 = tkinter.Label(window, text = "", fg = "green")
lb4.place(x=160, y = 330)

entry_a = []
entry_b = []

window.mainloop()