import PyQt5.QtWidgets as QtWidgets

class Settings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.show_window()

    def show_window(self):
        self.resize(300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.show()
