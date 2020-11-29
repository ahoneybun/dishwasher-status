#!/usr/bin/python3

import sys
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QToolTip, QWidget, QApplication
from PyQt5.QtCore    import *


class Dishwasher(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):      

        QToolTip.setFont(QFont('SansSerif', 10))

        btn1 = QPushButton("Clean", self)
        btn1.setToolTip('Press this button to set status to clean')
        btn1.resize(btn1.sizeHint())
        btn1.move(30, 50)

        btn2 = QPushButton("Dirty", self)
        btn2.setToolTip('Press this button to set status to dirty')
        btn2.resize(btn2.sizeHint())
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()

        self.showMaximized()
        self.setWindowTitle('Dishwasher Status')
        self.show()
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage('Dishwasher is ' + sender.text())
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Dishwasher()
    sys.exit(app.exec_())