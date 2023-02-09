from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Lev Zigomet")
        self.setGeometry(300,300,400,400)
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Lev Zigomet2")
        self.main_text.move(150,150)
        self.main_text.adjustSize()
        self.button = QtWidgets.QPushButton(self)
        self.button.move(300,300)
        self.button.adjustSize()
        self.button.clicked.connect(self.button_pressed)
        self.button.setText("ziga")
        i = 0
    def button_pressed(self):
        print("salam")

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()
