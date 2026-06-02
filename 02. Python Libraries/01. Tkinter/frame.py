from tkinter import *

app = Tk()

app.geometry("600x600")

frame1 = Frame(app,relief=SUNKEN,bg="white",border=5,padx=40)
frame2 = Frame(app,relief=SUNKEN,bg="white",border=5,pady=40)

frame1.pack(side=LEFT,fill=Y,anchor="nw")
frame2.pack(side=TOP,fill=X,anchor="ne")

lab1 = Label(frame1,text="Hello World")
lab2 = Label(frame2,text="hello World")
lab1.pack()
lab2.pack()

app.mainloop();