import pygame as pg
import numpy as np
import random as rd
from os import listdir
from os.path import isfile, join




class Grid:

    def __init__(self, cols: int, rows: int):
        self.table = [[Node(row, col)
                       for col in range(cols)]
                      for row in range(rows)]
        self.cols = cols
        self.rows = rows

    def draw_map(self, screen: "PyGame screen"):
        """Draws whole map"""
        screen.fill(Node.BLACK)
        for row in self.table:
            for node in row:
                node.draw(screen)

    def change_field(self, row: int, col: int, f_type: int):
        self.table[row][col].change_field_type(f_type)
    
    def generate_trash(self,row: int, col: int):
        self.table[row][col].generate_trash()

    def draw_node(self, screen, row: int, col: int):
        self.table[row][col].draw(screen)
    
    def get_trash_possition(self, trash: int):
        trash_possition = []
        for row in self.table:
            for node in row:
                if node.field_type == trash and node.house.empty == False:
                    trash_possition.append((node.row,node.col))
        return trash_possition
    
    def garbage_to_collect(self):
        garbage = []
        field_types = []
        d = rd.randint(1,7)
        day = self.table[0][0].house.get_day_of_week(d)
        for index, x in enumerate(day):
            if index != 0 and index != 1:
                garbage.append(x)
        print(garbage)
        print("Today is:", day[1], ", garbage to collect: ",end = '')
        for x in garbage:
            print(x[2],", ",end='')
            field_types.append(x[0])
        return field_types




class House:
    # define some basic colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    SKYBLUE = (0,191,255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    PINK = (199,21,133)
    GREY = (192,192,192)

    #define trash 
    paper = (5,WHITE,"paper")
    glass = (6,SKYBLUE,"glass")
    metal = (7,GREY,"metal")
    plastic = (8,ORANGE,"plastic")

    #define days of the week
    MONDAY = (1, "Monday", paper, metal)
    TUESDAY = (2, "Tuesday", glass)
    WEDNESDAY=(3, "Wednesday", plastic, metal)
    THURSDAY = (4, "Thursday", glass)
    FRIDAY = (5, "Friday", paper, metal)
    SATURDAY = (6, "Saturday", plastic)
    SUNDAY = (7, "Sunday", metal)
    DAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]


    def __init__(self):
        self.empty = True
        self.trash = None
        self.trash_file = None
            
    def find_trash_file(self, trash):
        trash_files_list = []

        file_names = [f for f in listdir("Images\\TestImages") if isfile(join("Images\\TestImages", f))]
        #filter names
        for f in file_names:
            if trash[2] in f:
                trash_files_list.append(f)
        
        f = rd.randint(0,len(trash_files_list))
        return trash_files_list[f-1]

    def generate_trash(self):
        self.empty = False
        num = rd.randint(1, 4)
        if num == 1:
            self.trash = self.paper
            self.trash_file = self.find_trash_file(self.trash)
        elif num == 2:
            self.trash = self.glass
            self.trash_file = self.find_trash_file(self.trash)
        elif num == 3:
            self.trash = self.metal
            self.trash_file = self.find_trash_file(self.trash)
        elif num == 4:
            self.trash = self.plastic
            self.trash_file = self.find_trash_file(self.trash)

    def get_day_of_week(self, d: int):
        for day in self.DAYS:
            if day[0] == d:
                return day



class Node:
    # define rectangles dimensions
    r_width = 20
    r_height = 20
    r_margin = 5

    # define some basic colors
    # TODO: change to Enum
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    SKYBLUE = (0,191,255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    PINK = (199,21,133)
    GREY = (192,192,192)


    def __init__(self, row: int, col: int,
                 field_type: int = 0):
        self.row = row
        self.col = col
        self.field_type = field_type
        self.house = House()
        self.house.generate_trash()
        print(self.house.trash,self.house.trash_file)



    def draw(self, screen):
        color = self.get_field_color()
        col = self.col
        row = self.row
        width = self.r_width
        height = self.r_height
        margin = self.r_margin
        # rect -> (left, top, width, height)
        # draw.rect(surface, color, rect, margin)
        pg.draw.rect(screen, color,
                     ((col * (width + margin)) + margin,
                      (row * (height + margin)) + margin,
                      width, height))
        pg.display.flip()  # refresh screen
    
    def generate_trash(self):
        self.house.generate_trash()
        self.field_type = self.house.trash[0]


    def change_field_type(self, field_type: int):
        self.field_type = field_type

    def get_field_color(self) -> tuple:
        """Gets the color tuple of field"""
        #base color
        if self.field_type == 0:
            return self.GREEN
        #truck color
        elif self.field_type == 1:
            return self.RED
        #end point
        elif self.field_type == 2:
            return self.BLUE
        #obstacles color
        elif self.field_type == 3:
            return self.ORANGE
        #path color
        elif self.field_type == 4:
            return self.PINK
        #paper
        elif self.field_type == 5:
            return self.WHITE
        #glass
        elif self.field_type == 6:
            return self.SKYBLUE
        #metal 
        elif self.field_type == 7:
            return self.GREY
        #plastic 
        elif self.field_type == 8:
            return self.ORANGE
