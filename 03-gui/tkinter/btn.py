from tkinter import *

app = Tk()

app.geometry("300x500")

def func():
    print("Hello world")

btn1 = Button(app,activebackground='blue',activeforeground='red',text="Button1",command=func,bd="3",padx=20,pady=20,width=50).place(x=20,y=20)

app.mainloop()