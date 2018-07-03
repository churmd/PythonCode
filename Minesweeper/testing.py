#!/usr/bin/env python3
import tkinter
import mineclass

if __name__ == "__main__":
        window = tkinter.Tk()
        window.title("Minesweeper")
        game = mineclass.Game(window)
        window.mainloop()
