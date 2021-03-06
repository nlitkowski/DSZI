import pygame as pg
import numpy as np
import random as rd
from os import listdir
from os.path import isfile, join
# from Logic.TrashRecognition.ImageClassification import classify

# MODULE LEVEL VARIABLES
recognized_trash = {

}
# trash_files = classify()
########################


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
        print("\n Today is:", day[1], ", garbage to collect: ",end = '')
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
    trash_dict = {
        "paper": (5, WHITE, "paper"),
        "glass": (6, SKYBLUE, "glass"),
        "metal": (7, GREY, "metal"),
        "plastic": (8, ORANGE, "plastic")
    }
    #define days of the week
    MONDAY = (1, "Monday", trash_dict["paper"], trash_dict["metal"])
    TUESDAY = (2, "Tuesday", trash_dict["glass"])
    WEDNESDAY=(3, "Wednesday", trash_dict["plastic"], trash_dict["metal"])
    THURSDAY = (4, "Thursday", trash_dict["glass"])
    FRIDAY = (5, "Friday", trash_dict["paper"], trash_dict["metal"])
    SATURDAY = (6, "Saturday", trash_dict["plastic"])
    SUNDAY = (7, "Sunday", trash_dict["metal"])
    DAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]


    def __init__(self):
        self.empty = True
        self.trash = None
        self.trash_file = None

            
    def find_trash_file(self):
        from os.path import sep # culture and os invariant separator
        
        file_names = [(join(f"Images{sep}TestImages", f))
             for f in listdir(f"Images{sep}TestImages") 
             if isfile(join(f"Images{sep}TestImages", f))]

        file_name = file_names[rd.randint(0,len(file_names)) - 1]

        from Logic.TrashRecognition.ImageClassification import classify_file

        if file_name in recognized_trash:
            rt = recognized_trash[file_name]
            return (file_name, rt[0], rt[1])
        else:
            classification = classify_file(file_dir=file_name)
            recognized_trash[file_name] = (classification[1], classification[2])
            return classification 

    def generate_trash(self):
        self.empty = False
        
        classification = self.find_trash_file()
        self.trash = self.trash_dict[classification[1]]
        self.trash_file = classification[0]

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
