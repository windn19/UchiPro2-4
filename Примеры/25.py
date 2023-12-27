import sys

from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 100)
        self.button = QPushButton('Тест', parent=self)
        self.button.clicked.connect(self.action)
        self.button.move(60, 35)
        self.counter = 0

    def action(self):
        self.button.setText(str(self.counter))
        self.counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
