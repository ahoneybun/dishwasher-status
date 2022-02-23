#!/usr/bin/python3

import sys
from subprocess import call

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import Qt

class Dishwasher(QMainWindow):

    def __init__(self, parent=None):
        super(Dishwasher, self).__init__(parent)

        widget = QWidget(self)

        QToolTip.setFont(QFont('SansSerif', 10))

        btn1 = QPushButton("Clean", self)
        # btn1.resize(25, 25)
        btn1.setMaximumSize(75, 45)
        btn1.setToolTip('Press this button to set status to clean')
        btn1.clicked.connect(self.buttonClicked1)
        # btn1.move(30, 50)

        btn2 = QPushButton("Dirty", self)
        btn2.setMaximumSize(75, 45)
        btn2.resize(25, 25)
        btn2.setToolTip('Press this button to set status to dirty')
        btn2.clicked.connect(self.buttonClicked2)
        self.setCentralWidget(widget)
        # btn2.move(150, 50)

        # Building the Layout
        hlayout = QHBoxLayout()
        hlayout.setAlignment(Qt.AlignCenter)
        widget.setLayout(hlayout)
        hlayout.addWidget(btn1)
        hlayout.addWidget(btn2)

        self.statusBar()

        self.showMaximized()
        self.setWindowTitle('Dishwasher Status')
        self.show()

    def buttonClicked1(self):

        sender = self.sender()
        self.statusBar().showMessage('Dishwasher is ' + sender.text())
        call(['espeak "The dishwasher is clean" 2>/dev/null'], shell=True)

    def buttonClicked2(self):

        sender = self.sender()
        self.statusBar().showMessage('Dishwasher is ' + sender.text())
        call(['espeak "The dishwasher is dirty" 2>/dev/null'], shell=True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Dishwasher()
    sys.exit(app.exec_())
