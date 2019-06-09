from UI.grid import Grid
from UI.window import Window
from UI.settings import Settings
import PyQt5.QtWidgets as QtWidgets

def main():
    import sys

    #app = QtWidgets.QApplication(sys.argv)
    #Settings()
    #sys.exit(app.exec_())
    # initialize grid
    grid = Grid(20, 20)
    # initialize window (grid, start,end,mode)
    # mode 1 - random obstacles
    # mode 2 - board obstacles
    Window(grid, (0, 0), (19, 19), 1)


if __name__ == "__main__":
    main()
