from tkinter import *

app = Tk()

app.geometry("400x600")
app.maxsize(100,200)
app.minsize(400,600)

img = PhotoImage(file="images\img4.png")
title = Label(text="This is Heading")
imgpk = Label(image=img)
title.pack()
imgpk.pack()

app.mainloop()

