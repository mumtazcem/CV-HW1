#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a menubar. The
menubar has one menu with an exit action.

Author: Jan Bodnar
Website: zetcode.com
Last edited: January 2017
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.group_box = GroupBox(self)
        self.setCentralWidget(self.group_box)

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        openInputAct = QAction(QIcon('open.png'), '&Open Input', self)
        openInputAct.setShortcut('Ctrl+A')
        openInputAct.setStatusTip('Open Input Image')
        openInputAct.triggered.connect(lambda: self.open_input())

        openTargetAct = QAction(QIcon('open.png'), '&Open Target', self)
        openTargetAct.setShortcut('Ctrl+T')
        openTargetAct.setStatusTip('Open Target Image')
        openTargetAct.triggered.connect(lambda: self.open_target())

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openInputAct)
        fileMenu.addAction(openTargetAct)
        fileMenu.addAction(exitAct)

        self.button()


        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle('Histogram Equalization')
        self.show()

    def open_input(self):
        print('Opening Input...')
        # do the stuff
        #sys.exit(app.exec_())

    def open_target(self):
        print('Opening Target...')
        # do the stuff
        #sys.exit(app.exec_())

    def button(self):
        btn = QPushButton("Equalize Histogram", self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 0)


class GroupBox(QGroupBox):
    # IT SHOULD BE QGROUPBOX
    def __init__(self, parent):
        super(GroupBox, self).__init__(parent)

        self.init_groupbox()

    def init_groupbox(self):

        #gbox = QGroupBox(self)

        left = QGroupBox(self)
        left.setTitle('Input')
        left.setGeometry(30, 30, 550, 1150)

        middle = QGroupBox(self)
        middle.setTitle('Target')
        middle.setGeometry(650, 30, 550, 1150)

        right = QGroupBox(self)
        right.setTitle('Result')
        right.setGeometry(1280, 30, 550, 1150)


        """leftimg = QLabel(self)
        leftpixmap = QPixmap('color1.png')
        leftimg.setPixmap(leftpixmap)"""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())