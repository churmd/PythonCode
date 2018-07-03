#!/usr/bin/env python3
import tkinter
import random

class Cell(tkinter.Button):
    """A button that represents a cell on the board."""

    def __init__(self, master, game, row, col):
        """Creates the button and places it in the grid."""
        tkinter.Button.__init__(self, master)
        self.clicked = False
        onClick = lambda : game.cellClicked(row, col)
        self.config(text = " ", command = onClick,
                    bg = "blue", fg = "black", height = 1,
                     width = 1, disabledforeground = "black")
        self.grid(row=row, column=col)

    def revealMine(self):
        """Shows an X on the button and disables it."""
        self.clicked = True
        self.config(text = "X", state = "disabled", bg = "red")

    def revealNum(self, number):
        """Shows the supplied number on the button and disables it."""
        self.clicked = True
        self.config(text = str(number), state = "disabled", bg = "gray")

class Game(tkinter.Frame):
    """A frame with all the UI and logic for a Minesweeper game."""

    def __init__(self, master):
        """Initialises frame, starting setting and UI."""
        tkinter.Frame.__init__(self, master)
        self.pack()

        #Initial game options
        self.bSize = 8
        self.numMine = 10
        self.cellDict = {}
        self.buttons = {}
        self.clickCount = 0

        self.initUI()

        self.newBoard()

    def initUI(self):
        """Sets up the UI for the frame."""
        #Top bar with game status
        self.top = tkinter.Frame(self)
        self.top.pack()
        self.clicks = tkinter.Label(self.top, text = "Clicks" + str(self.clickCount))
        self.clicks.pack(side = tkinter.LEFT, anchor = tkinter.W, padx = (10, 50))
        self.gameState = tkinter.Label(self.top, text = "")
        self.gameState.pack(side = tkinter.RIGHT, anchor = tkinter.E, padx = (50, 10))

        #Button grid of the game
        self.grid = tkinter.Frame(self)
        self.grid.pack()

        #Bottom bar with reset/difficulty options
        self.options = tkinter.Frame(self)
        self.options.pack()
        self.reset = tkinter.Button(self.options, text = "Reset", command = self.newBoard)
        self.reset.pack(side = tkinter.LEFT)
        self.easy = tkinter.Button(self.options, text = "Easy", command = self.easyBoard)
        self.easy.pack(side = tkinter.LEFT)
        self.medium = tkinter.Button(self.options, text = "Medium", command = self.mediumBoard)
        self.medium.pack(side = tkinter.LEFT)
        self.hard = tkinter.Button(self.options, text = "Hard", command = self.hardBoard)
        self.hard.pack(side = tkinter.LEFT)

    def surCells(self, coord):
        """Returns the surrounding coordinates of a coordinate.
        Includes diagonal corners.
        Does not returns mine coordinatesself.
        Does not return coordinates outside board size."""
        (row, col) = coord
        rows = range(row-1, row+2)
        cols = range(col-1, col+2)
        inBounds = lambda x,y : x>=0 and y>=0 and x<self.bSize and y<self.bSize
        isMine = lambda x,y : self.cellDict[(x,y)] == -1
        sur = [(x,y) for x in rows for y in cols if inBounds(x,y) and not isMine(x,y)]
        return sur

    def newBoard(self):
        """Creates a new board."""
        self.clickCount= 0
        self.gameState.config(text = "")
        self.clicks.config(text = "Clicks: " + str(self.clickCount))
        self.cellDict = {}
        self.buttons = {}

        for b in self.grid.grid_slaves():
            b.destroy()
        self.buttons = {}
        self.cellDict = {}

        sz = range(self.bSize)
        self.cellDict = {(x,y) : 0 for x in sz for y in sz}
        mines = random.sample(range(self.bSize*self.bSize), self.numMine)
        for m in mines:
            cell = divmod(m, self.bSize)
            self.cellDict[cell] = -1
            for sur in self.surCells(cell):
                self.cellDict[sur] += 1
        self.buttons = {(x,y) : Cell(self.grid,self,x,y) for x in sz for y in sz}

    def cellClicked(self, row, col):
        """Handles what happens when a grid button is clicked."""
        self.clickCount += 1
        self.clicks.config(text = "Clicks: " + str(self.clickCount))
        coord = (row, col)
        val = self.cellDict[coord]
        if val == -1:
            for mine in self.getMines():
                self.buttons[mine].revealMine()
            self.disableAll()
            self.gameState.config(text = "Loss")
        else:
            self.buttons[coord].revealNum(val)
            if self.isVictory():
                self.disableAll()
                self.gameState.config(text = "Victory")

    def getMines(self):
        """Returns all mine coordinates."""
        isMine = lambda vk : vk[0] == -1
        justCoord = lambda vk : vk[1]
        cellValKey = zip(self.cellDict.values(), self.cellDict.keys())
        mines = map(justCoord, filter(isMine, cellValKey))
        return mines

    def getNonMines(self):
        """Returns all non-mine coordinates."""
        isNotMine = lambda vk : vk[0] != -1
        justCoord = lambda vk : vk[1]
        cellValKey = zip(self.cellDict.values(), self.cellDict.keys())
        notMines = map(justCoord, filter(isNotMine, cellValKey))
        return notMines

    def isVictory(self):
        """Determines if the game has been won.
        True if all non mine buttons clickedself.
        False otherwise."""
        nonMines = self.getNonMines()
        buttons = [self.buttons.get(m) for m in  nonMines]
        for button in buttons:
            if not button.clicked:
                return False
        return True

    def disableAll(self):
        """Disbales all buttons in the grid."""
        for button in self.buttons.values():
            button.config(state = "disabled")

    def easyBoard(self):
        """Sets options for an easy board."""
        self.bSize = 8
        self.numMine = 10
        self.newBoard()

    def mediumBoard(self):
        """Sets options for a medium board."""
        self.bSize = 16
        self.numMine = 40
        self.newBoard()

    def hardBoard(self):
        """Sets options for a hard board."""
        self.bSize = 24
        self.numMine = 99
        self.newBoard()
