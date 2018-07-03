#!/usr/bin/env python3
import tkinter
import mineclass
"""The main file to run to launch a minesweeper game."""

if __name__ == "__main__":
    """Launches a window with a minesweeper game."""
    window = tkinter.Tk()
    window.title("Minesweeper")
    game = mineclass.Game(window)
    window.mainloop()
