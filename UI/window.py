import pygame as pg
import time
from pygame.locals import *
from UI.grid import Grid


class Window():
    def __init__(self, grid):
        pg.init()
        # setup window
        pg.display.set_caption('Inteligentna śmieciarka')

        self.grid = grid
        # assign to variables for brevity
        cols = len(self.grid.cols)
        rows = len(self.grid.rows)
        width = self.grid.r_width
        height = self.grid.r_height
        margin = self.grid.r_margin

        screen_width = cols * (width + margin) + 2 * margin
        screen_height = rows * (height + margin) + 2 * margin

        self.screen = pg.display.set_mode([screen_width, screen_height])

        self.end = False

        self.clock = pg.time.Clock()
        grid.change_field(0, 0, 1)
        grid.change_field(19, 19, 2)
        path = [(i, i) for i in range(1, 20, 1)]
        self.grid.draw_map(self.screen)
        for t in path:
            x, y = t
            self.grid.change_field(x-1, y-1, 0)
            self.grid.change_field(x, y, 1)
            self.grid.draw_node(self.screen, x - 1, y - 1)
            self.grid.draw_node(self.screen, x, y)
            pg.time.delay(500)
        pg.quit()
