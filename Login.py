from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('500x200')
win.title('Login')
win.configure(bg = '#75ACEF')
win.resizable(0 , 0)


l1 = Label(win , text = 'name :' , bg = '#75ACEF' , fg = '#000000' , font = '30')
l1.place(x = 130 , y = 40)
l2 = Label(win , text = 'last name :' , bg = '#75ACEF' , fg = '#000000' , font = '30')
l2.place(x = 130 , y = 70)
l3 = Label(win , text = 'passworld :', bg = '#75ACEF' , fg = '#000000' , font = '30')
l3.place(x = 130 , y = 100)

e1 = Entry(win , font = '30')
e1.place(x = 180 , y = 40)
e2 = Entry(win , font = '30')
e2.place(x = 210 , y = 70)
e3 = Entry(win , font = '30')
e3.place(x = 215 , y = 100)

b1 = Button(win , text = 'Login' , font = '30' , width = 20)
b1.place(x = 180 , y = 130)

win.mainloop()
