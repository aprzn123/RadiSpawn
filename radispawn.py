#!/usr/bin/env python3
from argparse import ArgumentParser
from json import load
from os import path
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QLabel

from radial_widget import RadialMenu, Wedge

class MainWindow(QMainWindow):
    def __init__(self, geom):
        QMainWindow.__init__(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(geom)

        self.frame = QFrame()
        self.vbox = QVBoxLayout()

        self.menu = RadialMenu([
                Wedge("Firefox", 0xff720c, "firefox"),
                Wedge("Steam", 0x7999e5, "steam"),
                Wedge("Nautilus", 0xffffff, "nautilus")
                ])

        self.vbox.addWidget(self.menu, Qt.AlignCenter, Qt.AlignCenter)
        self.frame.setLayout(self.vbox)
        self.setCentralWidget(self.frame)

        self.showMaximized()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file", help="JSON file to define the menu; relative paths search pwd and then ~/.config/radispawn/")
    args = parser.parse_args()

    # fa stands for file argument
    fa = args.file
    json_file = None
    if path.exists(fa):
        json_file = fa
    # cf stands for .config file
    elif path.exists(cf := path.expanduser(f"~/.config/radispawn/{fa}")) and fa[0] != "/":
        json_file = cf
    else:
        raise FileNotFoundError(f"json file {fa} not found")
    

    app = QApplication(sys.argv)
    window = MainWindow(app.primaryScreen().availableGeometry())
    sys.exit(app.exec())
