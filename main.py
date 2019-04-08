import pygame as pg
import numpy as np

from UI.grid import Grid
from UI.window import Window


def main():
    # initialize grid
    grid = Grid(20, 20)
    # initialize window
    Window(grid) 


if __name__ == "__main__":
    main()
