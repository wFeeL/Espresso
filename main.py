import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QColorDialog


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1100, 400, 800, 500)
        self.setWindowTitle('Coffee')

        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        self.button.clicked.connect(self.show_result)

    def show_result(self):
        result = self.cur.execute('SELECT * FROM coffee '
                                  'ORDER BY id')
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
