import sys
from PyQt4.QtGui import *

class FirstWindow(QWidget):
    def __init__(self, parent=None):
        super(FirstWindow, self).__init__(parent)
        self.CPSBTN = QPushButton("text2", self)

class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.ToolsBTN = QPushButton('text', self)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.startFirstWindow()

    def startFirstWindow(self):
        self.ToolTab = FirstWindow(self)
        self.setWindowTitle("First Page")
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.CPSBTN.clicked.connect(self.startSecondWindow)
        self.show()

    def startSecondWindow(self):
        self.Window = SecondWindow(self)
        self.setWindowTitle("Second Page")
        self.setCentralWidget(self.Window)
        self.Window.ToolsBTN.clicked.connect(self.startFirstWindow)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())