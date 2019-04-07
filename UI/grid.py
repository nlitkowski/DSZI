import pygame as pg
import numpy as np


class Grid:
    # define rectangles dimensions
    r_width = 20
    r_height = 20
    r_margin = 5

    # define some basic colors
    # TODO: change to Enum
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, cols, rows):
        self.table = np.zeros(shape=(rows, cols), dtype=int)
        self.cols = list(range(cols))
        self.rows = list(range(rows))

    def draw_map(self, screen):
        screen.fill(self.BLACK)
        for col in self.cols:
            for row in self.rows:
                self.draw_node(screen, row, col)

    def draw_node(self, screen, row, col):
        if self.table[row][col] == 0:
            color = self.GREEN
        elif self.table[row][col] == 1:
            color = self.RED
        elif self.table[row][col] == 2:
            color = self.BLUE
        # rect -> (left, top, width, height)
        # draw.rect(surface, color, rect, margin)

        pg.draw.rect(screen, color,
                     ((col * (self.r_width + self.r_margin)) + self.r_margin,
                      (row * (self.r_height + self.r_margin)) + self.r_margin,
                      self.r_width, self.r_height))
        pg.display.flip()

    def change_field(self, row, col, field_type):
        self.table[row][col] = field_type
