import pygame as pg
import numpy as np
import random
import itertools as it
import math
from UI.grid import Grid, Node
from Logic.Apath import a_path


class Window():
    def __init__(self, grid: Grid,start: (int,int),end: (int,int),mode: int):





        
        
        
        self.start = start
        self.end = end
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
        

        def obstacles(self, grid: Grid,option: int):
            if option == 1:
                for x in range(len(grid.table)*2):
                    grid.generate_trash(random.randint(1,len(grid.table)-1),random.randint(1,len(grid.table)-1))
            elif option == 2:
                for x in range (13):
                    grid.change_field(x,14,3)
                for x in range (8):
                    grid.change_field(12,x+6,3)
                


        obstacles(self,grid,mode)
        grid.change_field(start[0], start[1], 1)
        grid.change_field(end[0], end[1], 2)

        

        #list of trash to collect
        to_collect = grid.get_trash_possition(5)
        print("to collect len: ",len(to_collect))

        #sort list of tuples to get minimum distance betwen all of them 
        #fajnie jakby sie udalo to zrobic wydajniej ale narazie niech bedzie tak 
        sorted(to_collect)

        pg.init()   # pylint: disable=no-member
        # setup window
        pg.display.set_caption('Inteligentna śmieciarka')
        
        #draw starting map
        self.grid.draw_map(self.screen)


        #move of the truck 
        def move_truck(path):
            for index, t  in enumerate(path):
                x,y =t
                if index != 0:
                    self.grid.change_field(path[index-1][0],path[index-1][1],4)
                self.grid.change_field(x, y, 1)
                self.grid.draw_node(self.screen, path[index-1][0],path[index-1][1])
                self.grid.draw_node(self.screen, x, y)
                pg.time.delay(500)


        #visit all points from from to_collect
        for ind, x in enumerate(to_collect):
            #copy table
            obs = [3,8,6,7]
            if ind == 0:
                array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
                path = a_path(array,(start[0],start[1]),(x[0],x[1]),obs)
                print("Path:",path)
            else:
                array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
                path = a_path(array,(to_collect[ind-1][0],to_collect[ind-1][1]),(x[0],x[1]),obs)
                print("Path:",path)

    
            #draw movement of garbage truck
            move_truck(path)


        #last move
        array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
        path = a_path(array,(to_collect[len(to_collect)-1][0],to_collect[len(to_collect)-1][1]),(end[0],end[1]),obs)
        print("Path:",path)
        move_truck(path)

        pg.quit()   # pylint: disable=no-member
