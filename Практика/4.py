import sys

from PyQt6.QtWidgets import (QApplication,
                             QLabel,
                             QWidget,
                             QPushButton,
                             QComboBox)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


years = ['крысы', 'быка', 'тигра', 'кота, кролика', 'дракона', 'змеи',
         'лошади', 'козы', 'обезьяны', 'петуха', 'собаки', 'свинья']


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('В год кого ты родился?')
        self.resize(240, 180)
        self.label = QLabel('Выбери год рождения:', self)
        self.comboBox = QComboBox(self)
        self.labelResult = QLabel('Ты родился в год ...', self)
        self.labelResult.resize(200, 20)
        self.button = QPushButton('Показать ответ', self)
        self.button.clicked.connect(self.action)
        self.label.move(30, 20)
        self.comboBox.move(30, 50)
        self.button.move(30, 80)
        self.labelResult.move(30, 120)
        self.setComboBox()

    def setComboBox(self):
        self.comboBox.addItems([str(i) for i in range(1900, 2024)])

    def action(self):
        index = (int(self.comboBox.currentText()) - 1900) % 12
        self.labelResult.setText(f'Ты родился в год {years[index]}.')


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
