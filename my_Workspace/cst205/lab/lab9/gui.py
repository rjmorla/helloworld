import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        box = QVBoxLayout()

        self.button = QPushButton("Button 1", self)
        self.button_label = QLabel('Button 1 not pushed')
        self.button.clicked.connect(self.on_click)
        self.button.setIcon(QtGui.QIcon('Hamburger_icon.svg.png'))

        self.button2 = QPushButton("Button 2", self)
        self.button2_label = QLabel('Button 2 not pushed')
        self.button2.clicked.connect(self.on_click2)

        box.addWidget(self.button)
        box.addWidget(self.button_label)
        self.setLayout(box)

        box.addWidget(self.button2)
        box.addWidget(self.button2_label)
        self.setLayout(box)

    @pyqtSlot()
    def on_click(self):
        self.button_label.setText('Button 1 pushed')

    def on_click2(self):
        self.button2_label.setText('Button 2 pushed')

app = QApplication(sys.argv)
win = MainWindow()

win.setWindowTitle("Roy Morla")
label = QLabel(win)

win.show()
sys.exit(app.exec())
