# Напиши программу для перевода единиц измерения температур между °C, °F и K, используя PyQt.
# Пользователь вводит одно любое значение температуры, в °C, °F или K. Программа выводит значения температур в двух
# других единицах измерения. Если пользователь вводит неверное значение или заполняет больше одного поля, то программа
# должна вывести сообщение об ошибке.

import sys

from PyQt6.QtWidgets import (QApplication,
                             QLabel,
                             QWidget,
                             QLineEdit,
                             QPushButton)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор температур')
        self.resize(320, 130)
        self.label = QLabel('Введите температуру!', self)
        self.labelC = QLabel('Температура °C', self)
        self.labelF = QLabel('Температура °F', self)
        self.labelK = QLabel('Температура K', self)
        self.entryC = QLineEdit(self)
        self.entryK = QLineEdit(self)
        self.entryF = QLineEdit(self)
        self.button = QPushButton('Пересчет', self)
        self.button.clicked.connect(self.action)
        self.labelC.move(20, 20)
        self.entryC.move(160, 20)
        self.labelF.move(20, 40)
        self.entryF.move(160, 40)
        self.labelK.move(20, 60)
        self.entryK.move(160, 60)
        self.label.move(20, 90)
        self.button.move(160, 90)

    def action(self):
        tempC = self.entryC.text()
        tempF = self.entryF.text()
        tempK = self.entryK.text()
        if len(list(filter(lambda x: x, [tempC, tempF, tempK]))) != 1:
            self.label.setText('Ошибка!')
            return
        if tempC and tempC.isdigit():
            tempF = (int(tempC) * 9 / 5) + 32
            tempK = int(tempC) + 273
        elif tempF and tempF.isdigit():
            tempC = (int(tempF) - 32) * 5 / 9
            tempK = (int(tempF) - 32) * 5 / 9 + 273
        elif tempK and tempK.isdigit():
            tempC = int(tempK) - 273
            tempF = (int(tempK) - 273) * 9 / 5 + 32
        else:
            self.label.setText('Ошибка!')
            return
        self.entryC.setText(f'{tempC}')
        self.entryF.setText(f'{tempF}')
        self.entryK.setText(f'{tempK}')

        self.label.setText('')


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
