import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

color = ""

my_dict = { "Pick a color": {"RGB": (0, 0, 0), "HEX":"#00000"},
            "RED": [{"RGB": (255, 0, 0),
                     "HEX":"#FF000"}
                   ],
            "GREEN": [{"RGB": (0,255,0),
                      "HEX": "#FF020"}]}


class Window(QWidget):
    def __init__(self, num):
        super().__init__()
        if num == 1:
            self.label1 = QLabel("CST 205 Color Exchange!")
            self.my_combo_box = QComboBox()
            self.my_combo_box.addItems(my_dict)
            self.label2 = QLabel("")
            self.label3 = QLabel("")
            self.btn = QPushButton("Show Color", self)


            vbox = QVBoxLayout()
            vbox.addWidget(self.label1)
            vbox.addWidget(self.my_combo_box)
            vbox.addWidget(self.btn)

            hbox = QHBoxLayout()
            hbox.addWidget(self.label2)
            hbox.addWidget(self.label3)

            mbox = QVBoxLayout()
            mbox.addLayout(vbox)
            mbox.addLayout(hbox)
            self.setLayout(mbox)

            self.my_combo_box.currentIndexChanged.connect(self.RGB)
            self.my_combo_box.currentIndexChanged.connect(self.HEX)
            self.btn.clicked.connect(self.on_click)
        else:
            print(type(color))
            self.setStyleSheet("background-color: %s;"  % color)


    @pyqtSlot()
    def RGB(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        try:
            self.label2.setText(f'RGB: {my_dict[my_text][0]["RGB"]}')
        except:
            self.label2.setText("")
        print(my_text)
        global color
        colot = my_text

    def HEX(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        try:
            self.label3.setText(f'HEX: {my_dict[my_text][0]["HEX"]}')
        except:
            self.label3.setText("")
    def on_click(self):
        self.new_window = NewWindow()
        self.new_window.show()

class  NewWindow(Window):
    def __init__(self):
        super(NewWindow, self).__init__(2)
        self.setWindowTitle("Color")
        print(self.RGB) #########################3

app = QApplication(sys.argv)
main = Window(1)
main.setWindowTitle("Colors!")
main.show()
sys.exit(app.exec_())
