from UI.grid import Grid
from UI.window import Window


def main():
    # initialize grid
    grid = Grid(20, 20)
    # initialize window
    Window(grid,(0,0),(19,19))


if __name__ == "__main__":
    main()
