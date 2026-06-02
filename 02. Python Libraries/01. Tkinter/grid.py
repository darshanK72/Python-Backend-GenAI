from tkinter import *

app = Tk()

input1 = Label(app,text="Number1").grid(row=0,column=0,ipadx=20)
e1 = Entry(app).grid(row=0,column=1)
input2 = Label(app,text="Number2").grid(row=1,column=0,ipadx=20)
e2 = Entry(app).grid(row=1,column=1)
btn = Button(app,text="Submit").grid(row=2,column=0,columnspan=2,ipady=20)

app.mainloop()