#!/usr/bin/env python3
import tkinter
import random

class Cell(tkinter.Button):
    def __init__(self, master, symbol=" "):
        tkinter.Button.__init__(self, master)
        self.config(text = " ", command = self.reveal, bg = "blue")
        self.pack()
        self.symbol = symbol

    def reveal(self):
        print("Revealing!")
        self.config(text = self.symbol, bg = "red")

class Game(tkinter.Tk):
    def __init__(self):
            tkinter.Tk.__init__(self)
            self.buttons = [Cell(self, "Value " + str(i)) for i in range(10)]
            self.boardSize = 8
            self.mineNum = 10
            self.board = []

    def newBoard(self):
        board = [[0] * self.boardSize for _ in self.boardSize]
        mines = random.sample(range(self.boardSize*self.boardSize), self.mineNum)
        for m in mines:
            row, col = divmod(self.boardSize, m)
            board[row][column] = -1
            #TODO update surrounding coords

    def getSurCoords(self, row, col):
        rows = range(row-1, row+2)
        cols = range(col-1, col+2)
        inBounds = lambda x,y : x>0 and y>0 and x<self.boardSize and y<self.boardSize
        coords = [(x,y) for x in row for y in cols if inBounds(x,y)]
