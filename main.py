from UI.grid import Grid
from UI.window import Window


def main():
    # initialize grid
    grid = Grid(20, 20)
    # initialize window (grid, start,end,mode)
    #mode 1 - random obstacles
    #mode 2 - board obstacles
    Window(grid,(0,0),(19,19),2)


if __name__ == "__main__":
    main()
