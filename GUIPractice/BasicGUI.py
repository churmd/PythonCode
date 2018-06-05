import tkinter

top = tkinter.Tk()

class MyButton(tkinter.Button):
    def __init__(self):
        tkinter.Button.__init__(self, master=None)
        self.config(top, text="Hello", command = self.changeColour, bg = "blue")
        self.pack()

    def changeColour(self):
        print("Change colour")
        self.config(bg = "red")

button = MyButton()
top.mainloop()
