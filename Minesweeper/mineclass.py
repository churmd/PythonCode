#!/usr/bin/env python3
import tkinter
import random

class Cell(tkinter.Button):
    def __init__(self, master, row, col):
        tkinter.Button.__init__(self, master)
        onClick = lambda : master.cellClicked(row, col)
        self.config(text = " ", command = onClick, bg = "blue")
        self.grid(row=row, column=col)

    def reveal(self, symbol):
        self.config(text = symbol, state = "disabled", bg = "red")

class Game(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.bSize = 8
        self.numMine = 10
        self.cellDict = {}
        self.buttons = {}
        self.newBoard()

    def surCells(self, coord):
        (row, col) = coord
        rows = range(row-1, row+2)
        cols = range(col-1, col+2)
        inBounds = lambda x,y : x>=0 and y>=0 and x<self.bSize and y<self.bSize
        isMine = lambda x,y : self.cellDict[(x,y)] == -1
        sur = [(x,y) for x in rows for y in cols if inBounds(x,y) and not isMine(x,y)]
        return sur

    def newBoard(self):
        sz = range(self.bSize)
        self.cellDict = {(x,y) : 0 for x in sz for y in sz}
        mines = random.sample(range(self.bSize*self.bSize), self.numMine)
        for m in mines:
            cell = divmod(m, self.bSize)
            self.cellDict[cell] = -1
            for sur in self.surCells(cell):
                self.cellDict[sur] += 1
        self.buttons = {(x,y) : Cell(self,x,y) for x in sz for y in sz}

    def cellClicked(self, row, col):
        coord = (row, col)
        val = self.cellDict[coord]
        if val == -1:
            for mine in self.getMines():
                self.buttons[mine].reveal("X")
        else:
            self.buttons[coord].reveal(str(val))

    def getMines(self):
        isMine = lambda vk : vk[0] == -1
        justCoord = lambda vk : vk[1]
        cellValKey = zip(self.cellDict.values(), self.cellDict.keys())
        mines = map(justCoord, filter(isMine, cellValKey))
        return mines

    def getNonMines(self):
        isNotMine = lambda vk : vk[0] != -1
        justCoord = lambda vk : vk[1]
        cellValKey = zip(self.cellDict.values(), self.cellDict.keys())
        notMines = map(justCoord, filter(isNotMine, cellValKey))
        return notMines
