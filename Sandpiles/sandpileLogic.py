#!/usr/bin/env python3
import numpy as np

"""The logic for sandpile maths."""

class Sandpile():
    """Class to hold a sandpile number."""

    def __init__(self, list2D, maxHeight):
        self.array = np.array(list2D)
        self.maxHeight = maxHeight

def singlePass(sandpile):
    """Takes one pass over each element in the sandpile,
    toppling and piles too hight."""
    (row, col) = sandpile.array.shape
    nextSandpile = np.zeros((row, col), dtype = int)
    for r in range(row):
        for c in range(col):
            val = sandpile.array[r][c]
            if val > sandpile.maxHeight:
                nextSandpile[r][c] += (val - 4)
                if r + 1 < row:
                    nextSandpile[r + 1][c] += 1
                if r - 1 >= 0:
                    nextSandpile[r - 1][c] += 1
                if c + 1 < col:
                    nextSandpile[r][c + 1] += 1
                if c - 1 >= 0:
                    nextSandpile[r][c - 1] += 1
            else :
                nextSandpile[r][c] += val
    sandpile.array = nextSandpile
