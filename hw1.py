#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Mumtaz Cem Eris
150130129
11/10/2018
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import colorsys
from PIL import Image
from matplotlib import pyplot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


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
        input_image = QLabel(self)
        input_pixmap = QPixmap('color2.png')
        input_pixmap.height()
        input_image.setPixmap(input_pixmap)
        input_image.setGeometry(320 - input_pixmap.width() / 2
                                , 60, input_pixmap.height(),
                                input_pixmap.width())

        img_file = Image.open("color2.png").convert('RGB')
        img = img_file.load()
        [xs, ys] = img_file.size
        freq_r = {}
        freq_g = {}
        freq_b = {}
        for x in range(0, xs):
            for y in range(0, ys):
                [r, g, b] = img[x, y]
                freq_r[r] = freq_r.get(r, 0) + 1
                freq_g[g] = freq_g.get(g, 0) + 1
                freq_b[b] = freq_b.get(b, 0) + 1

        keylist = list(range(0,256))
        yaxis_r = list(range(0,256))
        yaxis_g = list(range(0,256))
        yaxis_b = list(range(0,256))
        for key in keylist:
            yaxis_r[key] = freq_r[key]
            yaxis_g[key] = freq_g[key]
            yaxis_b[key] = freq_b[key]

        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, yaxis_r, color="red")
        axis2.bar(keylist, yaxis_g, color="green")
        axis3.bar(keylist, yaxis_b, color="blue")
        fig.savefig('input_plots.png', dpi=83)

        input_imager = QLabel(self)
        input_pixmapr = QPixmap('input_plots.png')
        input_imager.setPixmap(input_pixmapr)
        input_imager.setGeometry(40, 350, input_pixmapr.width(), input_pixmapr.height())
        input_image.show()
        input_imager.show()


    def open_target(self):
        print('Opening Target...')
        input_image = QLabel(self)
        input_pixmap = QPixmap('color1.png')
        input_pixmap.height()
        input_image.setPixmap(input_pixmap)
        input_image.setGeometry(780, 60, input_pixmap.height(),
                                input_pixmap.width())

        img_file = Image.open("color1.png").convert('RGB')
        img = img_file.load()
        [xs, ys] = img_file.size
        freq_r = {}
        freq_g = {}
        freq_b = {}
        for x in range(0, xs):
            for y in range(0, ys):
                [r, g, b] = img[x, y]
                freq_r[r] = freq_r.get(r, 0) + 1
                freq_g[g] = freq_g.get(g, 0) + 1
                freq_b[b] = freq_b.get(b, 0) + 1

        keylist = list(range(0, 256))
        yaxis_r = list(range(0, 256))
        yaxis_g = list(range(0, 256))
        yaxis_b = list(range(0, 256))
        for key in keylist:
            yaxis_r[key] = freq_r[key]
            yaxis_g[key] = freq_g[key]
            yaxis_b[key] = freq_b[key]

        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, yaxis_r, color="red")
        axis2.bar(keylist, yaxis_g, color="green")
        axis3.bar(keylist, yaxis_b, color="blue")
        fig.savefig('target_plots.png', dpi=83)

        input_imager = QLabel(self)
        input_pixmapr = QPixmap('target_plots.png')
        input_imager.setPixmap(input_pixmapr)
        input_imager.setGeometry(650, 350, input_pixmapr.width(), input_pixmapr.height())
        input_image.show()
        input_imager.show()

    def button(self):
        btn = QPushButton("Equalize Histogram", self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 0)


class GroupBox(QGroupBox):
    def __init__(self, parent):
        super(GroupBox, self).__init__(parent)

        self.init_groupbox()

    def init_groupbox(self):

        left = QGroupBox(self)
        left.setTitle('Input')
        left.setGeometry(30, 30, 550, 1150)

        middle = QGroupBox(self)
        middle.setTitle('Target')
        middle.setGeometry(650, 30, 550, 1150)

        right = QGroupBox(self)
        right.setTitle('Result')
        right.setGeometry(1280, 30, 550, 1150)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())