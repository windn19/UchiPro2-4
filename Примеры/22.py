import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QWidget,
                             QLineEdit, QPushButton)


def action():
    label.setText(f'Привет, {entry.text()}!')


app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 100)

label = QLabel('Как тебя зовут?', parent=window)
entry = QLineEdit(parent=window)
button = QPushButton('Нажми меня!', parent=window)
label.move(150, 10)
entry.move(130, 30)
button.move(150, 60)

button.clicked.connect(action)

window.show()
sys.exit(app.exec())
