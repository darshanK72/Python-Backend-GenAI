from tkinter import *
# from PIL import  image,imageTk

app = Tk()

app.geometry("733x434")
app.minsize(400,300)
app.maxsize(800,600)

img = PhotoImage(file="images\img4.png")
imgpack = Label(image=img)
imgpack.pack()

app.mainloop()