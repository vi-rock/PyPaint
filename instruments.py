import random
from PyQt5.QtGui import QBrush, QColor, QPen
from Constant import SPRAY_PARTICLES_PER_TEN


class Instrument:  # Основной класс для инструментов
    def __init__(self, color, xs, ys, xe=None, ye=None, size=10, fill=False, style=None):
        self.start_point = (xs, ys)
        self.end_point = (xe, ye)
        self.fill = fill
        self.pen = QPen()
        self.pen.setWidth(size)
        self.pen.setColor(QColor(*color))
        if style:
            self.pen.setStyle(style)
        self.brush = QBrush(QColor(*color))


class BrushPoint(Instrument):
    def __init__(self, color, xs, ys, size=10):
        super(BrushPoint, self).__init__(color, xs, ys, size=size)
        self.size_of_brush = size

    def draw(self, painter):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(self.start_point[0] - self.size_of_brush // 2,
                            self.start_point[1] - self.size_of_brush // 2,
                            self.size_of_brush // 2, self.size_of_brush // 2)


class Line(Instrument):
    def __init__(self, color, xs, ys, xe, ye, size=10, style=None):
        super(Line, self).__init__(color, xs, ys, xe, ye, size, style=style)

    def draw(self, painter):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawLine(*self.start_point, *self.end_point)


class Circle(Instrument):
    def __init__(self, color, xs, ys, xe, ye, size=10, fill=False, style=None):
        super(Circle, self).__init__(color, xs, ys, xe, ye, size, fill, style)
        n = 255 if self.fill else 0
        self.brush = QBrush(QColor(*color, n))

    def draw(self, painter):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        radius = int(((self.start_point[0] - self.end_point[0]) ** 2
                      + (self.start_point[1] - self.end_point[1]) ** 2) ** 0.5)
        painter.drawEllipse(self.start_point[0] - radius, self.start_point[1] - radius, 2 * radius, 2 * radius)


class Rect(Instrument):
    def __init__(self, color, xs, ys, xe, ye, size=10, fill=False, style=None):
        super(Rect, self).__init__(color, xs, ys, xe, ye, size, fill, style)
        n = 255 if self.fill else 0
        self.brush = QBrush(QColor(*color, n))

    def draw(self, painter):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawRect(*self.start_point,
                         self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])


class Text(Instrument):
    def __init__(self, color, font, rect, horizontal, text):
        super().__init__(color=color, xs=None, ys=None)
        self.font = font
        self.text = text
        self.pos = rect
        self.horizontal = horizontal

    def draw(self, painter):
        painter.setPen(self.pen)
        painter.setFont(self.font)
        painter.drawText(self.pos, self.horizontal, self.text)


class CurvedLine:
    def __init__(self, list_points):
        self.list_points = list_points

    def draw(self, painter):
        for i in self.list_points:
            i.draw(painter)


class Spray(Instrument):
    def __init__(self, color, xs, ys, size=10):
        super(Spray, self).__init__(color, xs, ys, size=size)
        self.dot_pos = []
        self.pen.setWidth(1)
        for n in range(SPRAY_PARTICLES_PER_TEN * size):
            xo = int(random.gauss(0, size))
            yo = int(random.gauss(0, size))
            self.dot_pos.append((xo, yo))

    def draw(self, painter):
        painter.setPen(self.pen)
        for i in self.dot_pos:
            painter.drawPoint(int(self.start_point[0] + i[0]), int(self.start_point[1] + i[1]))
