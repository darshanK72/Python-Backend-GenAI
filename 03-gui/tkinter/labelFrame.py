from tkinter import *

app = Tk()

app.geometry("300x300")

f1 = LabelFrame(app,text="Heading")
f1.pack(fill="both",expand="yes")
l1 = Label(f1,text="This is First Frame")
l1.pack()
f2 = LabelFrame(app,text="Content")
f2.pack(fill="both",expand="yes")
l2 = Label(f2,text="This is Second frame")
l2.pack()

app.mainloop()