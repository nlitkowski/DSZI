import numpy as np
from heapq import *  # pylint: disable=unused-wildcard-import

class AStarNode():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def APath(table, start, end):

    # Create start and end node
    start_node = AStarNode(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = AStarNode(None, end)
    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)


    # Loop until you find the end
    i = 0
    while len(open_list) > 0:
        print(i)
        i=i+1
        current_node = open_list[0]
        current_index = 0

        # Find current node
        for index, item in enumerate(open_list):
            if(item.f < current_node.f):
                current_node = item
                current_index = index

        # Pop current off open list and add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found end node
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: 

            
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # If in maze
            if node_position[0] > (len(table) - 1) or node_position[0] < 0 or node_position[1] > (len(table[len(table)-1]) -1) or node_position[1] < 0:
                continue

            # If not obstacle
            if table[node_position[0]][node_position[1]].field_type == 3:
                continue

            
            new_node = AStarNode(current_node, node_position)
            children.append(new_node)

        
        for child in children:


            def InClosedlist(child: AStarNode):
                for closed_child in closed_list:
                    if child.position == closed_child.position:
                        return True
                    

            def InOpenlist(child: AStarNode):
                for open_node in open_list:
                    if child == open_node:
                        return True
                    

           
            # Child is on the closed list
            if InClosedlist(child)==True:
                continue

            child.g = current_node.g + 1
            child.h = max(abs(child.position[0] - end_node.position[0]), abs(child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            # Child is already in the open list
            if InOpenlist(child)==True:
                continue

            open_list.append(child)

        

           

        

