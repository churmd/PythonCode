#!/usr/bin/env python3
import tkinter

class MyButton(tkinter.Button):
    def __init__(self, top, text="Hello"):
        tkinter.Button.__init__(self, top)
        self.config(text=text, command = self.changeColour, bg = "blue")
        self.pack()

    def changeColour(self):
        print("Change colour for " + self.cget("text"))
        self.config(bg = "red")

class MyWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.buttons = [MyButton(self, "Button" + str(i)) for i in range(10)]

if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()
