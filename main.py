import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Constant import *
from mainWindow import Ui_MainWindow
from brushsettings import BrushSettingsWidget
from info import InfoWidget
from profile import ProfileWidget
from startDialog import StartDialogWidget
from textDialog import TextDialogWidget
from logindialog import LoginDialogWidget
from registerDialog import RegisterDialogWidget
from colorsettings import ColorSettingsWidget
from fontsettings import FontSettingsWidget
from instruments import *
from effects import *


class Canvas(QWidget):  # Главный класс отвечающий за рисование, холст
    def __init__(self, widget, user):
        super(Canvas, self).__init__(widget)
        self.user = user
        self.widget = widget
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        self.brush = cur.execute(f"SELECT name FROM Instrument "
                                 f"WHERE id = (SELECT instrument_id FROM User WHERE id = {self.user})").fetchone()[0]
        con.close()
        self.lbl = QLabel(self)

        self.font = QFont(*STANDARD_FONT)
        self.pen_style = None
        self.start_text_point = (0, 0)
        self.end_text_point = (0, 0)

        self.cancel_objects = list()
        self.objects = list()
        self.__line_count = 0

        self.__last_x, self.__last_y = None, None

        self.brush_size = 10
        self.fill = False

        self.basic_color = BLACK
        self.extra_color = WHITE

        self.image = QImage(QSize(*MAX_SIZE), QImage.Format_ARGB32)  # label не сможет быть больше этого размера
        self.image.fill(QColor(*self.extra_color))
        self.image_init(self.image)  # инициализация максимального размера полотна

    def image_init(self, img):
        self.image = QImage(img)
        self.lbl.resize(self.image.size())
        self.image = self.image.scaled(self.image.size(), Qt.IgnoreAspectRatio)
        self.widget.resize(self.lbl.size())
        self.lbl.setPixmap(QPixmap.fromImage(self.image))
        self.objects.clear()
        self.cancel_objects.clear()

    def paintEvent(self, event):
        canvas_painter = QPainter(self.lbl.pixmap())
        canvas_painter.begin(self)
        for i in self.objects:
            i.draw(canvas_painter)
        canvas_painter.end()

    def mousePressEvent(self, event):  # Рисование при нажатии
        if self.brush in (INSTRUMENTS[0], INSTRUMENTS[5], INSTRUMENTS[6]):
            if self.brush != INSTRUMENTS[6]:
                self.objects.append(BrushPoint(self.basic_color if self.brush == INSTRUMENTS[0] else self.extra_color,
                                               event.x(), event.y(), size=self.brush_size))
            else:
                self.objects.append(Spray(self.basic_color, event.x(), event.y(), self.brush_size))
            self.__line_count += 1
        elif self.brush == INSTRUMENTS[1]:
            self.objects.append(Line(self.basic_color, event.x(), event.y(), event.x(), event.y(),
                                     size=self.brush_size, style=self.pen_style))
        elif self.brush == INSTRUMENTS[2]:
            self.objects.append(Circle(self.basic_color, event.x(), event.y(), event.x(), event.y(),
                                size=self.brush_size, fill=self.fill, style=self.pen_style))
        elif self.brush == INSTRUMENTS[3]:
            self.objects.append(Rect(self.basic_color, event.x(), event.y(), event.x(), event.y(),
                                     self.brush_size, fill=self.fill, style=self.pen_style))
        elif self.brush == INSTRUMENTS[4]:
            self.start_text_point = (event.x(), event.y())
            c = self.lbl.pixmap().toImage().pixelColor(event.x(), event.y())
            self.objects.append(Rect((255 - c.red(), 255 - c.green(), 255 - c.blue()),
                                event.x(), event.y(), event.x(), event.y(),
                                size=1, fill=False, style=Qt.DashLine))

        elif self.brush in EFFECTS:
            if self.brush == EFFECTS[0]:
                img = Negative(self.lbl.pixmap().toImage()).draw()
            elif self.brush == EFFECTS[1]:
                img = Old(self.lbl.pixmap().toImage()).draw()
            elif self.brush == EFFECTS[2]:
                img = Noise(self.lbl.pixmap().toImage()).draw()
            elif self.brush == EFFECTS[3]:
                img = Sepia(self.lbl.pixmap().toImage()).draw()
            elif self.brush == EFFECTS[4]:
                factor, ok_pressed = QInputDialog.getInt(
                    self, "Введите коэффицент", "",
                    50, 30, 150, 1)
                if ok_pressed:
                    img = BlackWhite(self.lbl.pixmap().toImage(), factor).draw()
            self.image_init(img)
        self.update()

    def mouseReleaseEvent(self, e):  # Рисование при зажатии
        if self.brush in (INSTRUMENTS[0], INSTRUMENTS[5], INSTRUMENTS[6]):
            self.__last_x = None
            self.__last_y = None
            n = []
            for i in range(self.__line_count):
                n.append(self.objects.pop(-1))
            self.__line_count = 0
            self.objects.append(CurvedLine(n))
        if self.brush == INSTRUMENTS[4]:
            self.objects.pop(-1)
            self.update()
            self.lbl.setPixmap(QPixmap.fromImage(self.image))
            td = TextDialog(self.font)
            if td.exec_():
                values = td.get_values()
                self.objects.append(
                    Text(self.basic_color, self.font,
                         QRect(*self.start_text_point,
                               self.end_text_point[0] - self.start_text_point[0],
                               self.end_text_point[1] - self.start_text_point[1]), **values))
                self.start_text_point, self.end_text_point = (0, 0), (0, 0)
            self.update()

    def mouseMoveEvent(self, event):  # Рисование при отпускании мыши
        if self.brush in (INSTRUMENTS[0], INSTRUMENTS[5], INSTRUMENTS[6]):
            if self.__last_x is None:
                self.__last_x = event.x()
                self.__last_y = event.y()
                return
            if self.brush != INSTRUMENTS[6]:
                self.objects.append(
                    Line(self.basic_color if self.brush == INSTRUMENTS[0] else self.extra_color,
                         self.__last_x, self.__last_y, event.x(), event.y(), size=self.brush_size))
            else:
                self.objects.append(Spray(self.basic_color, event.x(), event.y(), self.brush_size))
            self.__line_count += 1
        elif self.brush == INSTRUMENTS[1]:
            self.objects[-1].end_point = (event.x(), event.y())
        elif self.brush == INSTRUMENTS[2]:
            self.objects[-1].end_point = (event.x(), event.y())
        elif self.brush == INSTRUMENTS[3]:
            self.objects[-1].end_point = (event.x(), event.y())
        elif self.brush == INSTRUMENTS[4]:
            self.end_text_point = (event.x(), event.y())
            self.objects[-1].end_point = (event.x(), event.y())
        self.lbl.setPixmap(QPixmap.fromImage(self.image))
        self.update()

        if self.brush == INSTRUMENTS[0] or self.brush == INSTRUMENTS[5]:
            self.__last_x = event.x()
            self.__last_y = event.y()

    def undo(self):  # Отмена действия
        if self.objects:
            self.cancel_objects.append(self.objects.pop(-1))
        if len(self.cancel_objects) == MAX_UNDO_LENGTH:
            self.cancel_objects.pop(0)
        self.lbl.setPixmap(QPixmap.fromImage(self.image))
        self.update()

    def redo(self):  # Возвращение
        if self.cancel_objects:
            self.objects.append(self.cancel_objects.pop(-1))
        self.lbl.setPixmap(QPixmap.fromImage(self.image))
        self.update()

    def set_brush(self, brush):  # Выбор действующей кисти
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(f"UPDATE User SET instrument_id = (SELECT id FROM Instrument WHERE name = '{brush}') WHERE name = "
                    f"(SELECT name FROM User WHERE id = {self.user})")
        con.commit()
        con.close()
        self.brush = brush


class PaintWindow(QMainWindow, Ui_MainWindow):  # Главный виджет, на нём расположен весь интерфейс
    def __init__(self):
        super(PaintWindow, self).__init__()
        self.user = self.connect_user()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon("logo.png"))
        self.widget.setStyleSheet("background-color: #999999;")
        self.canvas = Canvas(self.widget, self.user)
        self.setWindowTitle("PyPaint")
        self.actionSave.triggered.connect(self.save)
        self.actionLoad.triggered.connect(self.load)
        self.actionInfo.triggered.connect(self.show_info)
        self.actionProfile.triggered.connect(self.show_profile)
        self.actionCustom.triggered.connect(lambda: self.change_color('b'))
        self.actionUndo.triggered.connect(self.canvas.undo)
        self.actionRedo.triggered.connect(self.canvas.redo)
        self.actionBrush.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[0]))
        self.actionLine.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[1]))
        self.actionCircle.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[2]))
        self.actionSquare.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[3]))
        self.actionText.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[4]))
        self.actionEraser.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[5]))
        self.actionSpray.triggered.connect(lambda: self.canvas.set_brush(INSTRUMENTS[6]))
        self.actionNegative.triggered.connect(lambda: self.canvas.set_brush(EFFECTS[0]))
        self.actionBlackWhiteFilter.triggered.connect(lambda: self.canvas.set_brush(EFFECTS[1]))
        self.actionNoise.triggered.connect(lambda: self.canvas.set_brush(EFFECTS[2]))
        self.actionSepia.triggered.connect(lambda: self.canvas.set_brush(EFFECTS[3]))
        self.actionBlack_White.triggered.connect(lambda: self.canvas.set_brush(EFFECTS[4]))

        self.br = BrushSettings()
        self.br.sizelSlider.valueChanged.connect(self.change_brush_size)
        self.br.fillBox.stateChanged.connect(self.change_brush_fill)
        self.br.styleBox.stateChanged.connect(self.change_brush_style)
        self.tabWidget.addTab(self.br, "Brush")
        self.cl = ColorSettings()
        self.cl.base_button.clicked.connect(lambda: self.change_color('b'))
        self.cl.extra_button.clicked.connect(lambda: self.change_color('e'))
        self.update_color()
        self.tabWidget.addTab(self.cl, "Color")
        self.fl = FontSettings()
        self.fl.toolButton.clicked.connect(self.update_font)
        self.tabWidget.addTab(self.fl, "Font")

    def connect_user(self):
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        while True:
            lg = LoginDialog()
            if lg.exec_():
                result = cur.execute(f"SELECT id FROM User WHERE name = '{lg.get_values()}'").fetchone()
                if result:
                    con.close()
                    return result[0]
            else:
                break
        con.close()
        sys.exit()

    def save(self):
        file_path = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")[0]
        if file_path == "":
            return

        self.canvas.lbl.pixmap().toImage().save(file_path)
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(f"UPDATE User SET count_image = count_image + 1 WHERE name = "
                    f"(SELECT name FROM User WHERE id = {self.user})")
        con.commit()
        con.close()

    def load(self):
        start = StartDialog()
        if start.exec_():
            values = start.get_values()
            self.canvas.image_init(values['image'])
            self.canvas.basic_color = values['base_color']
            self.canvas.extra_color = values['extra_color']
            self.update_color()

    def show_info(self):
        self.info = Info()
        self.info.show()

    def show_profile(self):
        con = sqlite3.connect('data.db')
        self.prof = Profile(*con.cursor().execute(
            f"SELECT name, color, count_image FROM User WHERE id = {self.user}").fetchone())
        con.close()
        self.prof.show()

    def change_brush_size(self, n):
        self.canvas.brush_size = n

    def change_brush_fill(self, n):
        if n == Qt.Checked:
            self.canvas.fill = True
        else:
            self.canvas.fill = False

    def change_brush_style(self, n):
        if n == Qt.Checked:
            style, ok_pressed = QInputDialog.getItem(
                self, "Выберите стиль", "",
                ('Dash', 'DashDot', 'Dot', 'DashDotDot'), 0, False)
            if ok_pressed:
                self.canvas.pen_style = PEN_STYLES[style]
            else:
                self.canvas.pen_style = PEN_STYLES['Dash']
        else:
            self.canvas.pen_style = None

    def change_color(self, color):
        c = QColorDialog.getColor()
        if c.isValid():
            if color == 'b':
                self.canvas.basic_color = (c.red(), c.green(), c.blue())
            else:
                self.canvas.extra_color = (c.red(), c.green(), c.blue())
        self.update_color()

    def update_color(self):
        i = QImage(QSize(1, 1), QImage.Format_RGB32)
        i = i.scaled(self.cl.base_color.size(), Qt.IgnoreAspectRatio)
        i.fill(QColor(*self.canvas.basic_color))
        self.cl.base_color.setPixmap(QPixmap.fromImage(i))
        i.fill(QColor(*self.canvas.extra_color))
        self.cl.extra_color.setPixmap(QPixmap.fromImage(i))

    def update_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.canvas.font = font
        self.fl.label_2.setFont(font)


class Info(QWidget, InfoWidget):  # Виджет, предоставляющий информацию о горячих клавишах
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Info")


class BrushSettings(QWidget, BrushSettingsWidget):  # Виджет для настройки кисточки
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)


class ColorSettings(QWidget, ColorSettingsWidget):  # Виджет для выбора основного и дополнительного цвета
    def __init__(self):
        super(ColorSettings, self).__init__()
        self.setupUi(self)


class FontSettings(QWidget, FontSettingsWidget):  # Виджет для настройки шрифта
    def __init__(self):
        super(FontSettings, self).__init__()
        self.setupUi(self)


class StartDialog(QDialog, StartDialogWidget):  # Диалоговое окно для создания нового холста
    def __init__(self):
        super(StartDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Create new image")
        self.choose_file.clicked.connect(self.load)
        self.base = BLACK
        self.extra = WHITE
        self.update_color()
        self.size_canvas = NORMAL_SIZE
        self.size_x.setSpecialValueText(str(NORMAL_SIZE[0]))
        self.size_y.setSpecialValueText(str(NORMAL_SIZE[1]))
        self.basic_button.clicked.connect(lambda: self.change_color('b'))
        self.extr_button.clicked.connect(lambda: self.change_color('e'))

    def change_color(self, color):
        c = QColorDialog.getColor()
        if c.isValid():
            if color == 'b':
                self.base = (c.red(), c.green(), c.blue())
            else:
                self.extra = (c.red(), c.green(), c.blue())
        self.update_color()

    def update_color(self):
        i = QImage(QSize(1, 1), QImage.Format_RGB32)
        i = i.scaled(self.basic_color.size(), Qt.IgnoreAspectRatio)
        i.fill(QColor(*self.base))
        self.basic_color.setPixmap(QPixmap.fromImage(i))
        i.fill(QColor(*self.extra))
        self.extra_color.setPixmap(QPixmap.fromImage(i))
        self.update_image()

    def update_image(self):
        if self.file_path.text():
            i = QImage(self.file_path.text())
            i = i.scaled(self.view.size(), Qt.KeepAspectRatio)
        else:
            i = QImage(QSize(1, 1), QImage.Format_RGB32)
            i.fill(QColor(*self.extra))
            i = i.scaled(self.view.size(), Qt.IgnoreAspectRatio)
        self.view.setPixmap(QPixmap.fromImage(i))

    def load(self):
        file_path = QFileDialog.getOpenFileName(self, "Load Image", "",
                                                "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")[0]

        if file_path == "":
            return

        self.file_path.setText(file_path)
        self.update_image()

    def get_values(self):
        if self.file_path.text():
            i = QImage(self.file_path.text())
        else:
            i = QImage(int(self.size_x.text()), int(self.size_y.text()), QImage.Format_RGB32)
            i.fill(QColor(*self.extra))
        return {'base_color': self.base,
                'extra_color': self.extra,
                'image': i}


class TextDialog(QDialog, TextDialogWidget):  # Диалоговое окно для вставки текста
    def __init__(self, font):
        super(TextDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Create text")
        self.hor = Qt.AlignLeft
        self.update_text()
        self.horBox.currentTextChanged.connect(self.horizontal)
        self.textEdit.textChanged.connect(self.update_text)
        self.label.setFont(font)

    def horizontal(self, sig):
        self.hor = HORIZONTAL[sig]
        self.update_text()

    def update_text(self):
        self.label.setText(self.textEdit.toPlainText())
        self.label.setAlignment(self.hor)

    def get_values(self):
        return {"horizontal": self.hor,
                "text": self.textEdit.toPlainText()}


class LoginDialog(QDialog, LoginDialogWidget):  # Диалоговое окно для вхождения в аккаунт
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.registr.clicked.connect(self.open_register)

    def open_register(self):
        rd = RegisterDialog()
        if rd.exec_():
            rd.register()

    def get_values(self):
        return self.user_name_label.text()


class RegisterDialog(QDialog, RegisterDialogWidget):  # Диалоговое окно регистрации
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Register")
        self.ccolor = (100, 10, 77)
        self.color_button.clicked.connect(self.change_color)
        self.user_name_label.textEdited.connect(self.update)

    def paintEvent(self, event):
        p = QPainter(self)
        p.begin(self)
        p.setBrush(QBrush(QColor(*self.ccolor, 255)))
        p.setFont(QFont("Impact", 40))
        p.drawRect(QRect(10, 50, 141, 141))
        p.setBrush(QBrush(QColor(0, 0, 0)))
        if self.user_name_label.text():
            p.drawText(QRect(10, 50, 141, 141), Qt.AlignCenter, self.user_name_label.text()[0].upper())
        p.end()

    def change_color(self):
        c = QColorDialog.getColor()
        if c.isValid():
            self.ccolor = (c.red(), c.green(), c.blue())

    def register(self):
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        if not cur.execute(f"SELECT id FROM User WHERE name = '{self.user_name_label.text()}'").fetchone():
            cur.execute(
                f"INSERT INTO User(name, color) VALUES('{self.user_name_label.text()}',"
                f"'{' '.join(list(map(str, self.ccolor)))}')")
        con.commit()
        con.close()


class Profile(QWidget, ProfileWidget):  # Виджет для отображения основной информации профиля
    def __init__(self, name, color, image_count):
        super(Profile, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Profile")
        self.name = name
        self.ccolor = color
        self.user_name_label.setText(name)
        self.user_image_count.setText(str(image_count))

    def paintEvent(self, event):
        p = QPainter(self)
        p.begin(self)
        p.setBrush(QBrush(QColor(*list(map(int, self.ccolor.split())), 255)))
        p.setFont(QFont("Impact", 40))
        p.drawRect(QRect(40, 20, 141, 141))
        p.setBrush(QBrush(QColor(0, 0, 0)))
        p.drawText(QRect(40, 20, 141, 141), Qt.AlignCenter, self.name[0].upper())
        p.end()


def except_hook(cls, exception, traceback):  # Отлов ошибок
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":  # Запуск программы
    app = QApplication(sys.argv)
    window = PaintWindow()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
