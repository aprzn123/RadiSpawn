#!/usr/bin/env python3
from argparse import ArgumentParser
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QLabel

from radial_widget import RadialMenu

class MainWindow(QMainWindow):
    def __init__(self, geom):
        QMainWindow.__init__(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(geom)

        self.frame = QFrame()
        self.vbox = QVBoxLayout()

        self.menu = RadialMenu()

        self.vbox.addWidget(self.menu, Qt.AlignCenter, Qt.AlignCenter)
        self.frame.setLayout(self.vbox)
        self.setCentralWidget(self.frame)

        self.showMaximized()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.parse_args()

    app = QApplication(sys.argv)
    window = MainWindow(app.primaryScreen().availableGeometry())
    sys.exit(app.exec())
