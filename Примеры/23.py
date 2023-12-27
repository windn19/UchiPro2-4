import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QWidget,
                             QLineEdit, QPushButton)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 100)
        self.label = QLabel('Как тебя зовут?', parent=self)
        self.entry = QLineEdit(parent=self)
        self.button = QPushButton('Нажми меня!', parent=self)
        self.button.clicked.connect(self.action)
        self.label.move(150, 10)
        self.entry.move(130, 30)
        self.button.move(150, 60)

    def action(self):
        self.label.setText(f'Привет, {self.entry.text()}!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
