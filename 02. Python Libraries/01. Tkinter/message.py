from tkinter import *
from tkinter import messagebox

app = Tk()

def fun1():
    messagebox.showinfo("information","Some Information")

def fun2():
    messagebox.showerror("error","Some error occured")

def fun3():
    messagebox.showwarning("warning","Warning")

def fun4():
    messagebox.askquestion("comfirm","Are you sure?")

app.geometry("600x600")

btn1 = Button(app,command=fun1,text="fun1").grid(row=1,column=3)
btn2 = Button(app,command=fun2,text="fun2").grid(row=2,column=3)
btn3 = Button(app,command=fun3,text="fun3").grid(row=3,column=3)
btn4 = Button(app,command=fun4,text="fun4").grid(row=4,column=3)

app.mainloop()