from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setGeometry(0, 0, *self.screen_size())
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(self.rect())

        # Set the window title
        self.setWindowTitle("Olympia Executor - Windows Edition")

def executor():
    print("Olympia windows version loaded")

app = QtWidgets.QApplication([])

window = QtWidgets.QMainWindow()

button = QtWidgets.QPushButton("Inject into roblox web version for windows")

def clicked():
    executor()

button.clicked.connect(clicked)

window.setCentralWidget(button)

window.show()

app.exec_()
