# Напиши программу для генерации безопасных паролей с помощью PyQt.
# Пользователь выбирает количество букв, цифр, символов и нажимает кнопку создать пароль. Программа выводит случайно
# сгенерированный пароль.
# Примечание: используй виджет QSpinBox.


import random
import string
import sys

from PyQt6.QtWidgets import (QApplication,
                             QLabel,
                             QWidget,
                             QPushButton,
                             QSpinBox,
                             QLineEdit)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Генератор паролей')
        self.resize(220, 220)
        self.label = QLabel('Ваш пароль: ', self)
        self.labelL = QLabel('Количество букв:', self)
        self.labelD = QLabel('Количество цифр:', self)
        self.labelP = QLabel('Количество символов:', self)
        self.entryL = QSpinBox(self)
        self.entryD = QSpinBox(self)
        self.entryP = QSpinBox(self)
        self.entryPassword = QLineEdit(self)
        self.button = QPushButton('Создать пароль', self)
        self.button.clicked.connect(self.action)
        self.labelL.move(20, 20)
        self.entryL.move(160, 20)
        self.labelD.move(20, 50)
        self.entryD.move(160, 50)
        self.labelP.move(20, 80)
        self.entryP.move(160, 80)
        self.button.move(20, 110)
        self.label.move(20, 140)
        self.entryPassword.move(20, 170)

    def action(self):
        lenLetters = int(self.entryL.text())
        lenDigits = int(self.entryD.text())
        lenPunct = int(self.entryP.text())
        letters = random.choices(string.ascii_letters, k=lenLetters)
        digits = random.choices(string.digits, k=lenDigits)
        punct = random.choices(string.punctuation, k=lenPunct)
        chars = letters + digits + punct
        random.shuffle(chars)
        password = ''.join(chars)
        self.entryPassword.setText(password)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
