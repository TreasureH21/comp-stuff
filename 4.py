from tkinter import *
def exit():
    root1 = Tk()
    label = Label(root1, text="Are you sure you want to exit?").grid(row=0, column=1)
    b1 = Button(root1, text="Yes",command=root1.quit).grid(row=1,column=1)
    b2 = Button(root1, text="No",command=root1.destroy).grid(row=1,column=2)
    root1.mainloop()

root = Tk()
button = Button(root, text="exit application", bg ="red", command=exit).pack()


root.mainloop()