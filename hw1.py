#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Mumtaz Cem Eris
150130129
11/10/2018
"""

import sys

import null as null
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import numpy as np
import colorsys
from PIL import Image
from matplotlib import pyplot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    input_r = list(range(0, 256))
    input_g = list(range(0, 256))
    input_b = list(range(0, 256))
    target_r = list(range(0, 256))
    target_g = list(range(0, 256))
    target_b = list(range(0, 256))

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
        self.input_r = list(range(0, 256))
        self.input_g = list(range(0, 256))
        self.input_b = list(range(0, 256))
        for key in keylist:
            self.input_r[key] = freq_r[key]
            self.input_g[key] = freq_g[key]
            self.input_b[key] = freq_b[key]
        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, self.input_r, color="red")
        axis2.bar(keylist, self.input_g, color="green")
        axis3.bar(keylist, self.input_b, color="blue")
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
        self.target_r = list(range(0, 256))
        self.target_g = list(range(0, 256))
        self.target_b = list(range(0, 256))
        for key in keylist:
            self.target_r[key] = freq_r[key]
            self.target_g[key] = freq_g[key]
            self.target_b[key] = freq_b[key]

        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, self.target_r, color="red")
        axis2.bar(keylist, self.target_g, color="green")
        axis3.bar(keylist, self.target_b, color="blue")
        fig.savefig('target_plots.png', dpi=83)

        input_imager = QLabel(self)
        input_pixmapr = QPixmap('target_plots.png')
        input_imager.setPixmap(input_pixmapr)
        input_imager.setGeometry(650, 350, input_pixmapr.width(), input_pixmapr.height())
        input_image.show()
        input_imager.show()


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

        btn = QPushButton('Equalize Histogram', self)
        btn.clicked.connect(self.result)
        btn.resize(btn.sizeHint())
        btn.move(0, 0)
        btn.setEnabled(True)

    def result(self):
        print('Clicked')

        img_file = Image.open("color2.png").convert('RGB')
        img = img_file.load()
        [xs, ys] = img_file.size
        ifreq_r = {}
        ifreq_g = {}
        ifreq_b = {}
        for x in range(0, xs):
            for y in range(0, ys):
                [r, g, b] = img[x, y]
                ifreq_r[r] = ifreq_r.get(r, 0) + 1
                ifreq_g[g] = ifreq_g.get(g, 0) + 1
                ifreq_b[b] = ifreq_b.get(b, 0) + 1

        sum_r = 0
        sum_g = 0
        sum_b = 0
        for x in range(0,256):
            sum_r = sum_r + ifreq_r[x]
            sum_g = sum_g + ifreq_g[x]
            sum_b = sum_b + ifreq_b[x]

        keylist = list(range(0, 256))
        input_r = list(range(0, 256))
        input_g = list(range(0, 256))
        input_b = list(range(0, 256))
        for key in keylist:
            input_r[key] = ifreq_r[key]/sum_r
            input_g[key] = ifreq_g[key]/sum_g
            input_b[key] = ifreq_b[key]/sum_b

        for key in keylist:
            if key is not 0:
                input_r[key] = input_r[key-1] + input_r[key]
                input_g[key] = input_g[key-1] + input_g[key]
                input_b[key] = input_b[key-1] + input_b[key]
        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, input_r, color="red")
        axis2.bar(keylist, input_g, color="green")
        axis3.bar(keylist, input_b, color="blue")
        fig.savefig('cdf_input.png', dpi=83)

        # TARGET

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
        sum_r = 0
        sum_g = 0
        sum_b = 0
        for x in range(0, 256):
            sum_r = sum_r + freq_r[x]
            sum_g = sum_g + freq_g[x]
            sum_b = sum_b + freq_b[x]
        keylist = list(range(0, 256))
        target_r = list(range(0, 256))
        target_g = list(range(0, 256))
        target_b = list(range(0, 256))
        for key in keylist:
            target_r[key] = freq_r[key]/sum_r
            target_g[key] = freq_g[key]/sum_g
            target_b[key] = freq_b[key]/sum_b

        for key in keylist:
            if key is not 0:
                target_r[key] = target_r[key-1] + target_r[key]
                target_g[key] = target_g[key-1] + target_g[key]
                target_b[key] = target_b[key-1] + target_b[key]

        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, target_r, color="red")
        axis2.bar(keylist, target_g, color="green")
        axis3.bar(keylist, target_b, color="blue")
        fig.savefig('cdf_target.png', dpi=83)

        lut_r = [0] * 256
        lut_g = [0] * 256
        lut_b = [0] * 256
        gj = 0
        for gi in range(256):
            while gj < 255 and target_r[gj] < input_r[gi]:
                gj = gj + 1
            lut_r[gi] = gj
        gj = 0
        for gi in range(256):
            while gj < 255 and target_g[gj] < input_g[gi]:
                gj = gj + 1
            lut_g[gi] = gj
        gj = 0
        for gi in range(256):
            while gj < 255 and target_b[gj] < input_b[gi]:
                gj = gj + 1
            lut_b[gi] = gj

        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, lut_r, color="red")
        axis2.bar(keylist, lut_g, color="green")
        axis3.bar(keylist, lut_b, color="blue")
        fig.savefig('result_plots.png', dpi=83)

        img_file = Image.open("color2.png").convert('RGB')
        img = img_file.load()
        [xs, ys] = img_file.size
        for x in range(0, xs):
            for y in range(0, ys):
                [r, g, b] = img[x, y]
                r = lut_r[r]
                g = lut_g[g]
                b = lut_b[b]
                img[x, y] = (r, g ,b)

        img_file.save('result_image.png')

        print('Opening Result...')
        result_image = QLabel(self)
        result_pixmap = QPixmap('result_image.png')
        result_pixmap.height()
        result_image.setPixmap(result_pixmap)
        result_image.setGeometry(1570 - result_pixmap.width() / 2
                                , 60, result_pixmap.height(),
                                 result_pixmap.width())

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
        result_r = list(range(0, 256))
        result_g = list(range(0, 256))
        result_b = list(range(0, 256))
        for key in keylist:
            if freq_r.get(key) is None:
                result_r[key] = 0
            else:
                result_r[key] = freq_r[key]
            if freq_g.get(key) is None:
                result_g[key] = 0
            else:
                result_g[key] = freq_g[key]
            if freq_b.get(key) is None:
                result_b[key] = 0
            else:
                result_b[key] = freq_b[key]

        fig = plt.figure()
        axis1 = fig.add_subplot(311)
        axis2 = fig.add_subplot(312)
        axis3 = fig.add_subplot(313)
        axis1.bar(keylist, result_r, color="red")
        axis2.bar(keylist, result_g, color="green")
        axis3.bar(keylist, result_b, color="blue")
        fig.savefig('result_histogram.png', dpi=83)

        resulth_image = QLabel(self)
        input_pixmapr = QPixmap('result_histogram.png')
        resulth_image.setPixmap(input_pixmapr)
        resulth_image.setGeometry(1300, 350, input_pixmapr.width(), input_pixmapr.height())

        result_image.show()
        resulth_image.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())