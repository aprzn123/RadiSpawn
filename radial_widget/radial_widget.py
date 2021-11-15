from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QPen, QBrush
from PySide6.QtCore import QRect, Qt

class Wedge:
    def __init__(self, label, color, call):
        self.label = label
        self.color = color
        self.call = call

class RadialMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.outer_radius = 200
        self.inner_radius = 100
        self.select_color = 0x000000
        self.wedges = [
                Wedge("Firefox", 0xff720c, "firefox"),
                Wedge("Steam", 0x7999e5, "steam"),
                Wedge("Nautilus", 0xffffff, "nautilus")
                ]
        self.selected_wedge = 0

        self.resize(self.outer_radius * 2, self.outer_radius * 2)
        self.setMinimumSize(self.outer_radius * 2, self.outer_radius * 2)

    def paintEvent(self, event):
        angle = 360 * 16 / len(self.wedges)
        base_angle = 90 * 16 - angle / 2

        painter = QPainter()
        painter.begin(self)

        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        for idx, wedge in enumerate(self.wedges):
            painter.setBrush(QBrush(wedge.color))
            painter.drawPie(0, 0, self.outer_radius * 2, self.outer_radius * 2, base_angle + angle * idx, angle)
            #painter.setCompositionMode(QPainter.CompositionModeSourceOut)
            #painter.drawPie(self.outer_radius - self.inner_radius, self.outer_radius - self.inner_radius, self.inner_radius * 2, self.inner_radius * 2, base_angle + angle * idx, angle)

        painter.setCompositionMode(QPainter.CompositionMode_DestinationOut)
        painter.drawEllipse(self.outer_radius - self.inner_radius, self.outer_radius - self.inner_radius, self.inner_radius * 2, self.inner_radius * 2)

        painter.end()
