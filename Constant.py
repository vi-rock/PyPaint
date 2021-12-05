from PyQt5.QtCore import Qt
with open(file='config.cfg', mode='r', encoding='utf-8') as f:  # Считывание данных из конфига
    r = f.readlines()
__values = dict()
for i in r:
    v = i.split()
    __values[v[0]] = tuple(map(int, v[1:]))
NORMAL_SIZE = __values['NORMAL_SIZE']
MAX_SIZE = __values['MAX_SIZE']
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPRAY_PARTICLES_PER_TEN = __values['SPRAY_PARTICLES_PER_TEN'][0]
MAX_UNDO_LENGTH = __values['MAX_UNDO_LENGTH'][0]
STANDARD_FONT = ("Times New Roman", 12)
PEN_STYLES = {"Dash": Qt.DashLine, "DashDot": Qt.DashDotLine, "Dot": Qt.DotLine, "DashDotDot": Qt.DashDotDotLine}
INSTRUMENTS = ("BrushPoint", "Line", "Circle", "Rect", "Text", "Eraser", "Spray")
EFFECTS = ("Negative", "Old", "Noise", "Sepia", "BlackWhite")
HORIZONTAL = {'Left': Qt.AlignLeft, 'Center': Qt.AlignHCenter, 'Right': Qt.AlignRight}
