import numpy as np
from heapq import *  # pylint: disable=unused-wildcard-import


def heuristic(a, b):

    x = abs(a[0]-b[0])
    y = abs(a[1]-b[1])

    if x > y:
        return 14*y + 10*(x - y)
    else:
        return 14*x + 10*(y - x)
    


def Astar(array, start, goal):

    
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    

    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []
    checked = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]
        checked.append(current)

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]

            return list(reversed(data)), checked
        print("array current",array[current[0],current[1]])
        array[current[0], current[1]]=2
        
        for i, j in neighbors:

            neighbor = current[0] + i, current[1] + j  

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array.flat[array.shape[1] * neighbor[0]+neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if array[neighbor[0]][neighbor[1]] == 2 and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
    return False