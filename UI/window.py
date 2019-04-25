import pygame as pg
import numpy as np
import random
from UI.grid import Grid, Node
from UI.Apath import Astar



class Window():
    def __init__(self, grid: Grid):
        pg.init()   # pylint: disable=no-member
        # setup window
        pg.display.set_caption('Inteligentna śmieciarka')

        self.grid = grid
        # assign to variables for brevity
        cols = self.grid.cols
        rows = self.grid.rows
        width = Node.r_width
        height = Node.r_height
        margin = Node.r_margin

        screen_width = cols * (width + margin) + 2 * margin
        screen_height = rows * (height + margin) + 2 * margin

        self.screen = pg.display.set_mode([screen_width, screen_height])

        self.end = False

        self.clock = pg.time.Clock()
        grid.change_field(0, 0, 1)
        grid.change_field(19, 19, 2)

        #random obsticle
        for x in range(40):
            grid.change_field(random.randint(1,18),random.randint(1,18),3)

        #path
        path = [(i, i) for i in range(1, 20, 1)]
        self.grid.draw_map(self.screen)

        #convert table to support Apath algoritm
        array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
        for i,x in enumerate(array):
            for j,y in enumerate(x):
                if y.field_type == 3:
                    array[i][j] = None
                
        nodes_array = np.array(array)

        #Run A star

        path, check = Astar(nodes_array, (0,0), (19, 19))
        print(path,"\n\n",check,"\n\n")


        for t in path:
            x, y = t
            self.grid.change_field(x-1, y-1, 0)
            self.grid.change_field(x, y, 1)
            self.grid.draw_node(self.screen, x - 1, y - 1)
            self.grid.draw_node(self.screen, x, y)
            pg.time.delay(500)
        pg.quit()   # pylint: disable=no-member

    


