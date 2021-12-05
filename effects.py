import random
from PyQt5.QtGui import QColor, QImage


class Effect:  # Основной класс для эффектов
    def __init__(self, image: QImage):
        self.image = image


class Negative(Effect):
    def __init__(self, image):
        super(Negative, self).__init__(image)

    def draw(self):
        size = self.image.size()
        for i in range(size.width()):
            for j in range(size.height()):
                col = self.image.pixelColor(i, j)
                self.image.setPixelColor(i, j, QColor(255 - col.red(), 255 - col.green(), 255 - col.blue()))
        return self.image


class Old(Effect):
    def __init__(self, image):
        super(Old, self).__init__(image)

    @staticmethod
    def __black_white_filter(pixel):
        r, g, b = pixel.red(), pixel.green(), pixel.blue()
        s = (r + g + b) // 3
        return s, s, s

    def draw(self):
        size = self.image.size()
        for i in range(size.width()):
            for j in range(size.height()):
                col = self.image.pixelColor(i, j)
                self.image.setPixelColor(i, j, QColor(*self.__black_white_filter(col)))
        return self.image


class Noise(Effect):
    def __init__(self, image):
        super(Noise, self).__init__(image)

    @staticmethod
    def __rand_noise(pixel):
        r, g, b = pixel.red(), pixel.green(), pixel.blue()
        return r + random.randint(0, 100), g + random.randint(0, 100), b + random.randint(0, 100)

    def draw(self):
        size = self.image.size()
        for i in range(size.width()):
            for j in range(size.height()):
                col = self.image.pixelColor(i, j)
                self.image.setPixelColor(i, j, QColor(*self.__rand_noise(col)))
        return self.image


class Sepia(Effect):
    def __init__(self, image):
        super(Sepia, self).__init__(image)

    @staticmethod
    def __sepia(pixel):
        r, g, b = pixel.red(), pixel.green(), pixel.blue()
        depth = 30
        s = (r + g + b) // 3
        r = s + depth * 2
        g = s + depth
        b = s
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255
        return r, g, b

    def draw(self):
        size = self.image.size()
        for i in range(size.width()):
            for j in range(size.height()):
                col = self.image.pixelColor(i, j)
                self.image.setPixelColor(i, j, QColor(*self.__sepia(col)))
        return self.image


class BlackWhite(Effect):
    def __init__(self, image, factor):
        super(BlackWhite, self).__init__(image)
        self.factor = factor

    def __black_white_filter(self, pixel):
        r, g, b = pixel.red(), pixel.green(), pixel.blue()
        if r + g + b > (((255 + self.factor) // 2) * 3):
            return 255, 255, 255
        return 0, 0, 0

    def draw(self):
        size = self.image.size()
        for i in range(size.width()):
            for j in range(size.height()):
                col = self.image.pixelColor(i, j)
                self.image.setPixelColor(i, j, QColor(*self.__black_white_filter(col)))
        return self.image
