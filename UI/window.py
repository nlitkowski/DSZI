import pygame as pg
import numpy as np
import random
from UI.grid import Grid, Node
from Logic.Apath import a_path


class Window():
    def __init__(self, grid: Grid,start: (int,int),end: (int,int)):

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
        

        def random_trash(grid: Grid):
            for x in range(len(grid.table)*2):
                grid.generate_trash(random.randint(1,len(grid.table)-1),random.randint(1,len(grid.table)-1))
                

        #generate trash
        random_trash(grid)
        grid.change_field(start[0], start[1], 1)
        grid.change_field(end[0], end[1], 2)

        #day of week (random)
        def garbage_to_collect():
            garbage = []
            field_types = []
            d = random.randint(1,7)
            day = grid.day_of_week(d)
            for index, x in enumerate(day):
                if index != 0 and index != 1:
                    garbage.append(x)
            print(garbage)
            print("Today is:", day[1], ", garbage to collect: ",end = '')
            for x in garbage:
                print(x[2],", ",end='')
                field_types.append(x[0])
            return field_types

        garbage = garbage_to_collect()

        #all obstacles, remove from list objects to collect
        obs = [3,5,6,7,8]
        for x in garbage:
            obs.remove(x)
      
        #list of garbage to collect
        to_collect = []
        for x in garbage:
            to_collect.extend(grid.get_trash_possition(x))
        print("\n",len(to_collect)," garbage to collect.")
        print(to_collect)

        #sort list of tuples to get minimum distance betwen all of them 
        
        #fajnie jakby sie udalo to zrobic wydajniej ale narazie niech bedzie tak 
        to_collect = sorted(to_collect)

        #window init
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
            print("collected:",grid.table[x][y].house.trash[2],"on possition: (",x,",",y,")  ", grid.table[x][y].house.trash_file)


        #visit all points from to_collect

        for ind, x in enumerate(to_collect):
            
            if ind == 0:
                array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
                path = a_path(array,(start[0],start[1]),(x[0],x[1]),obs)
                #print("Path:",path)
            else:
                array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
                path = a_path(array,(to_collect[ind-1][0],to_collect[ind-1][1]),(x[0],x[1]),obs)
                #print("Path:",path)

    
            #draw movement of garbage truck
            move_truck(path)


        #last move
        array = [[self.grid.table[col][row] for row in range(cols)] for col in range(rows)]
        path = a_path(array,(to_collect[len(to_collect)-1][0],to_collect[len(to_collect)-1][1]),(end[0],end[1]),obs)
        #print("Path:",path)
        move_truck(path)

        pg.quit()   # pylint: disable=no-member
